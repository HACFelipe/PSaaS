# PSaaS
This projects aims to materialize a complete software process. 

# Table of Contents
- [Requirements](#requirements)
  * [Requirements Elicitation](#requirements-elicitation)
  * [Requirements Traceability](#requirements-traceability)
  * [Requirements Validation](#requirements-validation)
- [Project](#project)
  * [Project Components](#project-components)
  * [Project Tasks](#project-tasks)
- [Building](#building)
  * [Building Blocks](#building-blocks)
    + [Code Blocks](#code-blocks)
    + [Concept Blocks](#concept-blocks)
- [Testing](#testing)
  * [Testing Components](#testing-components)
  * [Executor Components](#executor-components)
- [Deploying](#deploying)

## Requirements

Requirement are core components in the development process. The process can only start when the requirement elicitation and validation is complete. During the program it's necessary to define requirements in requirements elicitation, then you'll be able to set requirement traceability and finally the requirements are ready to be validated. When all requirements are validated you'll be able to proceed to the Project step.

### Requirements Elicitation

Requirements types are defined as Functional, Nonfunctional, Data, Domain and Business Rules. The program lets you define a requirement name, description and type. After defined, requirements can then be added to the project's requirement list being assigned a identifier. It's also possible to delete requirements from the project's requirement list.

### Requirements Traceability

Once the project's requirement list is defined, the program then takes you to the step of treceability set-up. It's not possible to set a traceability from a requirement to itself, however, it's possible to set traceability of every other requirement from the project's requirement list. Altough this is an optional step, requirements traceability are very common in software engineering process.

### Requirements Validation

In order to proceed to the Project step, it's mandatory all requirements from the project's requirement list are validated. The requirements need to be validated manually.

## Project

After validated, requirements need to be converted in projects. A project is necessary in order to make a requirement developable. The proccess of creating projects for requirements consists in enumerating tasks for a project in a way that, after the tasks are done the requirement can be satisfied. In this step, we define our projects using Project Components and Project Tasks.

### Project Components
Project commponents have a role of creating a construction plan for requirements to be built. They have name, description and a list of project tasks. It's possible to create as many as necessary project components. When a project component is defined it's then added to the project's project component list.

### Project Tasks

Project tasks have linked requirements, description, start date, due date, status and can also contain a list of project tasks, which we'll call project subtasks. After a project task is defined it can be assigned to a project component task list. Project subtasks can only reference tasks defined in the main project task. It's also not possible to overflow start and due dates of main project task in project subtasks.

## Building

After projects are defined, they need to be actually developed. The development of a project is made in the building step through building block components. When at least one defined project component exists in the project's project components list it's then possible to assign a project's component task to a building block component. You'll be able to proceed when at least one defined building block exists in the building block list.

### Building Blocks

By now, a building block can be either a code block or a concept block. Building blocks can have one single linked project task, a testability indicator and a description. After a building block component is defined its then added to a building block list.
#### Code Blocks

Code blocks are used in order to develop code for a project task. A code block has a source code, a executor component and may have expected results for test components.

#### Concept Blocks

When the task can not be solved with code, you can use a concept block to resolve the task. A concept block has a concept definition. 

## Testing

The testing step consists of validating if the building blocks that were built in the Building step agree with the expected results or definitions. Once at least a defined building block exists in the building block list, it can be tested by running a test component. You can only proceed when all the tests results of the test components in the test component list are valid.

### Testing Components

A test component have a linked building block component, a test result and may have test parameters. After a test component is defined, its then added to a test components list. When running a test component, the test runner receives a testable building block, with parameters, if needed, and a executor component. The executor component then executes the code received and returns a result. If the result is the same as the block expected results, the test result is set to success. 

#### Executor Components

An executor component has a code block and a programming language. The executor component executes the code block with the programming language and returns a result.

## Deploying

After all the tests results of the test components in the test component list are valid the program can then be deployed.

---

This projcet was developed for educational purposes and serves as evaluation practice for the Software Engineering Course given by [João Marcelo Borovina Josko][1] at [Feredal University of ABC (UFABC)][2] over the first four months of 2020. Main references of this projects were given by ["Pressman, R. S., & Maxim, B. R. (2015). Software engineering: A practitioner's approach. New York: McGraw-Hill H."][3]. It is being built using [HTML][4], [Python][5]'s library [Flask][6] with [Jinja][7], [CSS][8]'s framework [Bootstrap 4][9], [JavaScript][10]'s libraries [Popper.js][11] and [jQuery][12], jQuery's plugins [Bootstrap-Select][13] and [DataTables][14]. Icons given by [Font Awesome][15].

[1]: http://professor.ufabc.edu.br/~marcelo.josko/
[2]: http://ri.ufabc.edu.br/en/
[3]: https://www.worldcat.org/title/software-engineering-a-practitioners-approach/oclc/922972177?referer=di&ht=edition
[4]: https://www.w3.org/html/
[5]: https://www.python.org/
[6]: https://flask.palletsprojects.com/
[7]: https://jinja.palletsprojects.com/en/2.11.x/
[8]: https://www.w3.org/Style/CSS/
[9]: https://getbootstrap.com/
[10]: https://www.javascript.com/
[11]: https://popper.js.org/
[12]: https://jquery.com/
[13]: https://developer.snapappointments.com/bootstrap-select/
[14]: https://datatables.net/
[15]: https://fontawesome.com/
