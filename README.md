# Inductive Automation Ignition Persepective Framework

This is JAR Automation's Inheritable Ignition project. It adds contains pre-configured utility classes, components, and theming to make getting started with the perspective module even faster than it already is.

Click here to see a demo:

[ignition.jarautomation.io](https://ignition.jarautomation.io "JAR Automation Ignition Demo")

## Getting Started

The following assumes you've already successfully installed Inductive Ignition with the perspective module. If you need more information on how to do that, visit [Inductive University](https://inductiveuniversity.com). It also assumes you have a basic understanding of git and that you have a working git client.

The project relies on a custom css theme (which contains a single source of truth for colors, etc.) and some google fonts: Oswald, Basic and Lobster.

Navigate to the your ignition projects directory, typically:

Linux: `/usr/local/bin/ignition/data/projects`
Windows: `c:\Program Files\Inductive Automation\Ignition\data\projects`

Then clone this repository using:

`git clone https://github.com/joyja/ignition-framework.git {project_name}`

where `{project_name}` is the name you'd like your framework project to have.

The project relies on a custom css theme (which contains a single source of truth for colors, etc.) and some google fonts: Oswald, Basic and Lobster. These resources are all contained in the repository,
 but you'll have to copy them to the appropriate places for Ignition to register them properly.

Move the themes/jar.css and themes/jar folder to the themes directory, typically:

Linux: `/usr/local/bin/ignition/data/modules/com.inductiveautomation.perspective/themes`
Windows: `c:\Program Files\Inductive Automation\Ignition\data\modules/com.inductiveautomation.persepe
ctive/themes`

Move the fonts/Oswald, fonts/Basic, and fonst/Lobster folders to the fonts directory, typically:

Linux: `/usr/local/bin/ignition/data/modules/com.inductiveautomation.perspective/fonts`
Windows: `c:\Program Files\Inductive Automation\Ignition\data\modules/com.inductiveautomation.persepe
ctive/fonts`

Then restart your Ignition Gateway and the project will be registered by Ignition.

