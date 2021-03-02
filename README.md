# JAR Automation Ignition Perspective Framework

This is JAR Automation's Inheritable Ignition project. It adds contains pre-configured utility classes, components, and theme creation to make getting started with the perspective module even faster than it already is.

Click here to see a demo:

[ignition.jarautomation.io](https://ignition.jarautomation.io "JAR Automation Ignition Demo")

## Supporting the Framework

This framework is MIT-licensed and open source. If you're getting use out of it and you want to see it continue to grow, please consider [funding our open source work on Patreon.](https://www.patreon.com/jarautomation)

You can also help by contributing to the project (a contributing guide is in the works) or submitting issues.

## Getting Started

The following assumes you've already successfully installed Inductive Automation Ignition with the Perspective module. If you need more information on how to do that, visit [Inductive University](https://inductiveuniversity.com). It also assumes you have a basic understanding of git and that you have a working git client.

Navigate to the your ignition projects directory, typically:

- Linux: `/usr/local/bin/ignition/data/projects`
- Windows: `c:\Program Files\Inductive Automation\Ignition\data\projects`

Then clone this repository using:

`git clone https://github.com/joyja/ignition-framework.git {project_name}`

where `{project_name}` is the name you'd like your framework project to have.

The project relies on a custom css theme (which contains a single source of truth for colors, etc.) and some google fonts: Oswald, Basic and Lobster. These resources are all contained in the repository,
 but you'll have to copy them to the appropriate places for Ignition to register them properly.

Move the themes/jar.css file and the themes/jar folder to the themes directory, typically located at:

- Linux: `/usr/local/bin/ignition/data/modules/com.inductiveautomation.perspective/themes`
- Windows: `c:\Program Files\Inductive Automation\Ignition\data\modules\com.inductiveautomation.persepective\themes`

Move the fonts/Oswald, fonts/Basic, and fonts/Lobster folders to the fonts directory, typically located at:

- Linux: `/usr/local/bin/ignition/data/modules/com.inductiveautomation.perspective/fonts`
- Windows: `c:\Program Files\Inductive Automation\Ignition\data\modules\com.inductiveautomation.persepective\fonts`

Also upload the images in the image folder using Image Management in your Ignition Designer. Don't put the images in any folders, just upload them to the root directory.

Then restart your Ignition Gateway and the project will be registered by Ignition.
