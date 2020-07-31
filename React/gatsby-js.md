# Gatsby JS Notes

### Create project

```
gatsby new [project-name] [starter-repo-url]
Example:
gatsby new gatsby-bootcamp https://github.com/gatsbyjs/gatsby-starter-hello-world

```

## Gatsby Pages

All files in the directory `src/pages` represent pages such as the homepage, about, contact, etc.
When gatsby builds, it loops through `src/pages` and builds html pages for every file in the directory.

> `index.js` is the default name for the homepage

The default url for these pages come from the file name - `blog.js`'s url will be `/blog`

## Linking between pages

Use the `<Link>` component to link between pages. Below is an example:

```
import { Link } from 'gatsby';

<Link to="/contact">
  Contact Me
</Link>
```

## Higher-Order Component [Layout]

A convenient way to structure pages is to use a higher-order component, such as `<Layout>`:

```
[Layout.js]
const Layout = props => {
  return (
    <div className="layout">
      <Navbar />
      {props.children}
      <Footer />
    </div>
  )
}
```

Now wrap all your pages in this Layout component to re-use structure and styling.

## Gatsby Plugins

To use a plugin, install using npm (or w/e package manager) then include in the project's `gatsby-config.js` file's plugin array:

```
// gatsby-config.js
module.exports = {
  plugins: ["gatsby-plugin-sass"]
}
```

## GraphQL

While in development, Gatsby hosts a GraphQL sandbox on the url `localhost:8000/___graphql`.

### Site global variables:

- Stored in the `gatsby-config.js` file:

```
module.exports = {
  siteMetadata: {
    title: 'Full-Stack Bootcamp',
    author: "Tanner Langlinais"
  }
}
```

The `siteMetadata` is stored in the section "site/siteMetadata". So the GraphQL query will look like:

```
query MyQuery {
  site {
    siteMetadata {
      title
      author
    }
  }
}

Result:
{
  "data": {
    "site": {
      "siteMetadata": {
        "title": "Full-Stack Bootcamp",
        "author": "Tanner Langlinais"
      }
    }
  }
}
```

### Using GraphQL in a component

To use GraphQL in a React component, bring in `graphql` and `useStaticQuery` from the gatsby library. Assign the query to a variable, shown below:

```
  const data = useStaticQuery(graphql`
    query {
      site {
        siteMetadata {
          title
        }
      }
    }
  `)
```

The siteMetata variables are stored in `data.site.siteMetadata`.

## Using local files

The plugin `gatsby-source-filesystem` allows you to interact with local files. This requires more configuration, so we'll be passing in an object into the `gatsby-config.js` array `plugins`.

> Installation - `npm install --save gatsby-source-filesystem`

> The key `resolve` is a placeholder for the package name.

```
// gatsby-config.js
module.exports = {
  ...
    plugins: [
    "gatsby-plugin-sass",
    {
      resolve: "gatsby-source-filesystem",
      options: {
        name: "src",
        path: `${__dirname}/src/`,
      },
    },
  ],
}
```

This adds 2 new options to GraphQL: `file` and `allFile`. Now you can query local files inside components.

## Markdown & frontmatter

Gatsby looks at the top of every markdown file for a section called `frontmatter`. It's used for general data like titles, slugs, dates, etc. The frontmatter section is denoted by triple dashes "---":

```
// gatsby.md
---
title: "The Great Gatsby Bootcamp"
date: "2020-07-13"
---
This is the example blog post "gatsby.md"!.
```

### Rendering markdown

Use the plugin `gatsby-transformer-remark` to transform your markdown into html. Install and add to the gatsby-config.js plugins array.

Right away, you can fetch the markdown files from the GraphQL Explorer:

```
query MyQuery {
  allMarkdownRemark {
    edges {
      node {
        frontmatter {
          date
          title
        }
      }
    }
  }
}

Results:
{
  "data": {
    "allMarkdownRemark": {
      "edges": [
        {
          "node": {
            "frontmatter": {
              "date": "2020-07-13",
              "title": "The Great Gatsby Bootcamp"
            }
          }
        },
        {
          "node": {
            "frontmatter": {
              "date": "2020-07-01",
              "title": "React"
            }
          }
        }
      ]
    }
  }
}
```

## Node APIs

(https://www.gatsbyjs.org/docs/node-apis/)[https://www.gatsbyjs.org/docs/node-apis/]

Gatsby comes with a bunch of APIs for controlling your site's data.
These must be configured in a `gatsby-node.js` file.

> The `gatsby-node.js` file lives in the root directory.

- onCreateNode - This API is called when a new page node is created.

- createNodeField - Creates a field and attaches it to the specified node. The fields get stored in `fields`:

```
query MyQuery {
  allMarkdownRemark {
    nodes {
      fields {
        slug
      }
    }
  }
}
```

### Creating and attaching a slug to a node

Let's use the two APIs above to create and attach a slug field to every blog page:

```
module.exports.onCreateNode = ({ node, actions }) => {
  const { createNodeField } = actions

  // check to see if node is a blog (MarkdownRemark)
  if (node.internal.type === "MarkdownRemark") {
    const slug = path.basename(node.fileAbsolutePath, ".md")

    createNodeField({
      node,
      name: "slug",
      value: slug,
    })
  }
}
```

## Creating pages

Using the Node API `createPage`, we can dynamically create pages for every blog post. We need the file-path to the component, the url path to get to the page, and the context. The context is an object that gets passed to the template.

We can get the file-path using node `path`.

> The destructured `graphql` is NOT the same graphql we've been importing from 'gatsby'. This is Promise-based function to query.

Goals:

1. Get blogTemplate path (needed to pass into `createPage`)
2. Query all node slugs (blog-pages)
3. Call `createPage` for each slug. The template will fetch each page data

```
module.exports.createPages = async ({ graphql, actions }) => {
  const { createPages } = actions
  const blogTemplatePath = path.resolve("./src/templates/blog.js")
  const res = await graphql(`
    query {
      allMarkdownRemark {
        edges {
          node {
            fields {
              slug
            }
          }
        }
      }
    }
  `)

  res.data.allMarkdownRemark.edges.forEach(_edge => {
    createPages({
      component: blogTemplatePath,
      path: `/blog/${edge.node.fields.slug}`,
      context: {
        slug: edge.node.fields.slug,
      },
    })
  })
}
```

## Fetching blog info inside template

Because the blog templates are dynamic, we WON'T use `useStaticQuery` like before. You need to export a GraphQL query that Gatsby will run before creating the page.

```
export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        date
        title
      }
    }
  }
`
```

It will grab the context we defined in `gatsby-node.js`'s createPages function. It grabs the slug from the context and fetches the html, date and title for that specific page. Gatsby passes the returned data as a prop to the Blog component.

Entire `blog.js` template:

```
import React from "react"
import { graphql } from "gatsby"
import Layout from "../components/Layout/Layout"

export const query = graphql`
  query($slug: String!) {
    markdownRemark(fields: { slug: { eq: $slug } }) {
      html
      frontmatter {
        date
        title
      }
    }
  }
`

const Blog = props => {
  const blog = props.data.markdownRemark
  return (
    <Layout>
      <h1>{blog.frontmatter.title}</h1>
      <h2>{blog.frontmatter.date}</h2>
      <div dangerouslySetInnerHTML={{__html: blog.html}}>
      </div>
    </Layout>
  )
}

export default Blog
```

## Adding images

To use images inside of blog posts, let's install 3 packages:
`npm install gatsby-plugin-sharp gatsby-remark-images gatsby-remark-relative-images`

Configure them in `gatsby-config.js`:

```
module.exports = {
  siteMetadata: {
    title: "Full-Stack Bootcamp",
    author: "Tanner Langlinais",
  },
  plugins: [
    "gatsby-plugin-sass",
    {
      resolve: "gatsby-source-filesystem",
      options: {
        name: "src",
        path: `${__dirname}/src/`,
      },
    },
    "gatsby-plugin-sharp",
    {
      resolve: "gatsby-transformer-remark",
      options: {
        plugins: [
          "gatsby-remark-relative-images",
          {
            resolve: "gatsby-remark-images",
            options: {
              maxWidth: 750,
              linkImagesToOriginal: false,
            },
          },
        ],
      },
    },
  ],
}
```

- `gatsby-remark-relative-images` allows gatsby to find local images in markdown - ![Grass](./grass.png)

Now any markdown image will be included in the post!
