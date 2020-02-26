# Heroku Notes Summary

## Deploy

- Applications consist of your source code, a description of any dependencies, and a Procfile.
- Procfiles list process types - named commands that you may want executed.
- Deploying applications involves sending the application to Heroku using either Git, GitHub, or via an API.
- Buildpacks lie behind the slug compilation process. Buildpacks take your application, its dependencies, and the language runtime, and produce slugs.
- A slug is a bundle of your source, fetched dependencies, the language runtime, and compiled/generated output of the build system - ready for execution.
- Config vars contain customizable configuration data that can be changed independently of your source code. The configuration is exposed to a running application via environment variables.
- Add-ons are third party, specialized, value-added cloud services that can be easily attached to an application, extending its functionality.
- A release is a combination of a slug (your application), config vars and add-ons. Heroku maintains an append-only ledger of releases you make.

## Runtime

- Dynos are isolated, virtualized Unix containers, that provide the environment required to run an application.
- Your application’s dyno formation is the total number of currently-executing dynos, divided between the various process types you have scaled.
- The dyno manager is responsible for managing dynos across all applications running on Heroku.
- Applications that use the free dyno type will sleep after 30 minutes of inactivity. Scaling to multiple web dynos, or a different dyno type, will avoid this.
- One-off Dynos are temporary dynos that run with their input/output attached to your local terminal. They’re loaded with your latest release.
- Each dyno gets its own ephemeral filesystem - with a fresh copy of the most recent release. It can be used as temporary scratchpad, but changes to the filesystem are not reflected to other dynos.
- Logplex automatically collates log entries from all the running dynos of your app, as well as other components such as the routers, providing a single source of activity.
- Scaling an application involves varying the number of dynos of each process type.

# Heroku Notes Detailed

Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.

Apps are run on virtualized Unix containers that provide the environment required to run an application.

### How Heroku Works:

> An application consists of _source code_ and a description of any dependencies.
> Dependency format examples:

- Ruby = `Gemfile`
- Python = `requirements.txt`
- Node.js = `package.json`
- Java = `pom.xml`

The source code along with the dependency file should provide enough info for Heroku to build.

If you're running some established framework, Heroku can figure it out. For example, in Django it's `python <app>/manage.py` and in Node.js it's the `main` field in `package.json`.

## Procfiles

> `Procfiles` - list of commands that are executed by the app on startup.

Heroku apps include a `Procfile` that specifies the commands that are executed on startup. You can use a Procfile to declare a variety of process types, including:

- Your app's web server
- Multiple types of worker processes
- A singleton process, such as a clock
- Tasks to run before a new release is deployed

## Deployment

Heroku uses `git` as the primary method means for deployment. When you create an application on Heroku, it associates a new git remote, typically named `heroku`. All you have to do is push your code to the new remote:

```
$ git push heroku master
```

## Building Applications

When Heroku receives the app source code, it initiates a build of the source code. The build mechanism is language specific, but follows the same pattern - retrieving the specified dependencies, then creating any necessary assets (whether it be creating css files or compiling code).

> A `slug` is a bundle of your source, fetched dependencies, the language runtime, and compiled/generated output of the build system - ready for execution.

## Running applications on **dynos**

Heroku runs apps on a `dyno` that's been preloaded with your prepared `slug`.

> `Dyno` - isolated, virtualized Unix containers, that provide the environment required to run an application.

On first deployment, Heroku will run 1 dyno automatically. It will boot a dyno, load it with your slug, and execute the Procfile.

## Config vars

Heroku serves environment variables at runtime through `config vars`.

> `Config vars` contain customizable configuration data that can be changed independently of your source code. The configuration is exposed to a running application via environment variables.

All dynos in an application will have access to the same set of config vars at runtime.

Whenever you add, remove or change a `config var`, a new `release` is created.

## Releases

> `Release` - an append-only ledger of slugs and config vars

With this append-only ledger, managing your application is simple. Use the `heroku release` command to see the audit trail of release deploys:

```
$ heroku releases
== demoapp Releases
v103 Deploy 582fc95  jon@heroku.com   2013/01/31 12:15:35
v102 Deploy 990d916  jon@heroku.com   2013/01/31 12:01:12
```

Every time you deploy a new version of an application, a new slug is created and release is generated.

Heroku contains a store of previous releases, so it's easy to rollback and deploy a previous release.

```
$ heroku releases:rollback v102
Rolling back demoapp... done, v102
$ heroku releases
== demoapp Releases
v104 Rollback to v102 jon@heroku.com   2013/01/31 14:11:33 (~15s ago)
v103 Deploy 582fc95   jon@heroku.com   2013/01/31 12:15:35
v102 Deploy 990d916   jon@heroku.com   2013/01/31 12:01:12
```

## Dyno Manager

Part of the Heroku platform, the `dyno manager`, is responsible for keeping dynos running. Dynos are cycled at least once per day, or whenever a fault is detected in the running application.

> `Dyno Manager` - responsible for managing dynos across all applications running on Heroku.

The dyno cycling happens transparently and automatically, and is logged.

### **- Sleeping**

Applications that use the free dyno type will sleep. When a sleeping application received HTTP traffic, it will be awakened - causing a delay of a few seconds.

> One-off dynos are temporary dynos that can run with their input/output attached to your local terminal. They're loaded with your latest release.

Here's the simplest way to create and attach a one-off dyno:

```
$ heroku run bash
Running `bash` to terminal... up, run.8963
~ $ ls
```

This will spin up a new dyno, loaded with your release, then run the `bash` command - which will provide you with a Unix shell. Once you've terminated your session, or after a period of inactivity, the dyno will be removed.

Changes to the filesystem on one dyno are note propagated to other dynos and are not persisted across deploys and dyno restarts. A better and more scalable approach is to use a shared resource such as a database or queue.

> Each dyno gets its own _ephemeral filesystem_ - with a fresh copy of the most recent release. It can be used as a temporary scratchpad, but changes to the filesystem are not reflected to other dynos.

## Add-ons

Applications typicall make use of `add-ons` to provide backing services such as databases, queueing and caching systems, storage, email services and more. Add-ons are provided as a service by Heroku and third parties.

Heroku treats these add-ons as attached resources: provisioning an add-on is a matter of choosing one from the add-on marketplace, and attaching it to your application.

The interface between an add-on and your application is often provided by a `config var`.

> `Add-ons` are third party, specialized, value-added cloud services that can be easily attached to an application, extending its functionaltiy.

Much like `config vars`, whenever you add, remove or change an add-on, a new `release` is created.

## Logging and Monitoring

Heroku treats logs as streams of time-stamped events, and collates the stream of logs (produced from all processes running in all dynos) and the Heroku platform components into the `Logplex` - a high-perfomance, real-time system for log delivery.

> `Logplex` - automatically collates log entries from all running dynos of your app, as well as other components such as the routers, providing a single source of activity.

You can also dive into the logs from just a single dyno and keep the channel open:

```
$ heroku logs --ps web.1 --tail
2013-02-11T15:19:10+00:00 app[web.1]: Started GET "/" for 1.169.38.175 at 2013-02-11 15:19:10 +0000
```

Logplex keeps a limited buffer of logs for perfomance reasons. To persist them, and add action events - such as email notification on exception, use a `Loggin Add-on`.

## HTTP Routing

The dynos that ru process types named `web` are different in one way from all other dynos - they will receive HTTP traffic. Heroku's `HTTP routers` distribute incoming requests for your application across your running dynos.

Scaling an app's capacity to handle web traffic involves scaling the number of web dynos:

```
$ heroku ps:scale web+5
```

A random selection algorithm is used for HTTP request load balancing across web dynos - and handles both HTTP and HTTPS traffic. If also supports simultaneous connections, as well as timout handling.
