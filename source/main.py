from random import random, randint, sample
from datetime import date, timedelta

from entity.requirement import Requirement
from entity.requirement_list import RequirementList
from entity.project_task import ProjectTask
from entity.project import Project
from entity.project_list import ProjectList
from entity.building_block_list import BuildingBlockList
from entity.code import Code
from entity.concept import Concept
from entity.executor import Executor
from entity.test import Test
from entity.test_list import TestList

if __name__ == "__main__":

    #Customizable paramaters
    NUM_REQUIREMENTS = 25
    MIN_REQUIREMENTS_TRACEABILITY = 0
    MAX_REQUIREMENTS_TRACEABILITY = 8
    NUM_PROJECT_COMPONENTS = 6
    MIN_PROJECT_TASKS = 1
    MAX_PROJECT_TASKS = 6
    MIN_PROJECT_TASK_DURATION = 1;
    MAX_PROJECT_TASK_DURATION = 30;
    MIN_PROJECT_TASK_LINKED_REQUIREMENTS = 1;
    MAX_PROJECT_TASK_LINKED_REQUIREMENTS = 5;
    MIN_PROJECT_SUBTASKS = 0
    MAX_PROJECT_SUBTASKS = 6
    MIN_PROJECT_TASK_NESTING = 0
    MAX_PROJECT_TASK_NESTING = 4
    MIN_BUILDING_BLOCKS = 16
    MAX_BUILDING_BLOCKS = 32
    NUM_CODE_BLOCKS_PROPORTION = 0.7
    NUM_CONCEPT_BLOCKS_PROPORTION = 1 - NUM_CODE_BLOCKS_PROPORTION
    MIN_TEST_PARAMETERS = 0
    MAX_TEST_PARAMETERS = 3
    READY_TO_DEPLOY = False

    #[Step 0 - Requirements]
    project_requirements = RequirementList()

    #[Step 0.0 - Requirements Definition]
    requirement_types = ["Functional", "Nonfunctional", "Data", "Domain", "Business Rule"]

    #[Step 0.1 - Requirements Elicitation]
    input("\nYou are about to begin [Requirements Elicitation].\nPress Enter key to continue...")
    print("\n[Requirements Elicitation]")
    for i in range(NUM_REQUIREMENTS):
        requirement = Requirement(
            name = "Requirement %d" % (i),
            description = "Description of requirement %d" % (i),
            type = requirement_types[randint(0, len(requirement_types)) - 1])
        project_requirements.add_requirement(requirement)
    project_requirements.print_requirements()

    #[Step 0.2 - Requirements Traceability Definition]
    input("\nYou are about to begin [Requirements Traceability].\nPress Enter key to continue...")
    print("\n[Requirements Traceability]")
    for requirement in project_requirements.items:
        traceability = [req for req in project_requirements.items if req != requirement]
        traceability = sample(traceability, randint(MIN_REQUIREMENTS_TRACEABILITY, MAX_REQUIREMENTS_TRACEABILITY))
        requirement.traceability = traceability
    project_requirements.print_requirements_traceability()

    #[Step 0.3 - Requirements Validation]
    input("\nYou are about to begin [Requirements Validation].\nPress Enter key to continue...")
    print("\n[Requirements Validation]")
    for requirement in project_requirements.items:
        requirement.validate_requirement()
    project_requirements.print_requirements()

    #[Step 1 - Project]
    projects = ProjectList()
    
    #[Step 1.0 - Project Component Definition]
    for i in range(NUM_PROJECT_COMPONENTS):
        project = Project(
            name = "Project Component %d" % (i),
            description = "Description of Project Component %d" % (i))
        projects.add_project(project)

    #[Step 1.1 - Project Tasks Definition]
    input("\nYou are about to begin [Project Components Definition].\nPress Enter key to continue...")
    print("\n[Project Components Definition]")
    project_tasks = [] #This only exists to simplify Steps 2.0.0 and 2.0.1
    project_task = None
    for project in projects.items:
        for i in range(randint(MIN_PROJECT_TASKS, MAX_PROJECT_TASKS)):
            start_date = date.today() + timedelta(days = randint(MIN_PROJECT_TASK_DURATION, MAX_PROJECT_TASK_DURATION))
            due_date = start_date + timedelta(days = randint(MIN_PROJECT_TASK_DURATION, MAX_PROJECT_TASK_DURATION))
            linked_requirements = sample(project_requirements.items, randint(MIN_PROJECT_TASK_LINKED_REQUIREMENTS, MAX_PROJECT_TASK_LINKED_REQUIREMENTS))
            project_task = ProjectTask(
                description = "Task %d" % (i),
                start_date = start_date,
                due_date = due_date,
                linked_requirements = linked_requirements)
            project.add_task(project_task)
            project_tasks.append(project_task) #This only exists to simplify Steps 2.0.0 and 2.0.1
            
            #[Step 1.1.0 - Project Subtasks Definition]
            project_subtask = None
            for i in range(randint(MIN_PROJECT_TASK_NESTING, MAX_PROJECT_TASK_NESTING)):
                for j in range(randint(MIN_PROJECT_SUBTASKS, MAX_PROJECT_SUBTASKS)):
                    start_date = project_task.start_date + timedelta(days = randint(0, (project_task.due_date - project_task.start_date).days))
                    due_date = start_date + timedelta(days = randint(0, (project_task.due_date - start_date).days))
                    linked_requirements = sample(project_task.linked_requirements, randint(0, len(project_task.linked_requirements)))
                    project_subtask = ProjectTask(
                        description = "Subtask %d" % (j),
                        start_date = start_date,
                        due_date = due_date,
                        linked_requirements = linked_requirements)
                    project_task.add_subtask(project_subtask)
                    project_tasks.append(project_subtask) #This only exists to simplify Steps 2.0.0 and 2.0.1
                if project_subtask:
                        project_task = project_subtask

    projects.print_projects()

    #[Step 2 - Building]
    building_blocks = BuildingBlockList()

    #[Step 2.0 - Building Blocks Definition]
    input("\nYou are about to begin [Building Blocks Definition].\nPress Enter key to continue...")
    print("\n[Building Blocks Definition]")
    num_blocks = range(randint(MIN_BUILDING_BLOCKS, MAX_BUILDING_BLOCKS))
    num_code_blocks = int(NUM_CODE_BLOCKS_PROPORTION * num_blocks[-1])
    num_concept_blocks = int(NUM_CONCEPT_BLOCKS_PROPORTION * num_blocks[-1])

    #[Step 2.0.0 - Code Blocks Definition]
    input("\nYou are about to begin [Code Blocks Definition].\nPress Enter key to continue...")
    print("\n[Code Blocks Definition]")
    for i in range(num_code_blocks):
        testable = (random() >= 0.5)
        if testable:
            code = Code(
                description = "Description of Code %d" % (i),
                linked_project_task = project_tasks[randint(0, len(project_tasks) - 1)],
                source_code = "Source Code of Code %d" % (i),
                testable = testable,
                expected_results = ["Results for Code [%d]" % (i)])
        else:
            code = Code(
                description = "Description of Code %d" % (i),
                linked_project_task = project_tasks[randint(0, len(project_tasks) - 1)],
                source_code = "Source Code of Code %d" % (i))
        building_blocks.add_building_block(code)

    #[Step 2.0.1 - Concept Blocks Definition]
    input("\nYou are about to begin [Concept Blocks Definition].\nPress Enter key to continue...")
    print("\n[Concept Blocks Definition]")
    for i in range(num_concept_blocks):
        testable = (random() >= 0.5)
        if testable:
            concept = Concept(
                description = "Description of Concept %d" % (i),
                linked_project_task = project_tasks[randint(0, len(project_tasks) - 1)],
                concept_definition = "Definition of Concept %d" % (i),
                testable = testable)
        else:
            concept = Concept(
                description = "Description of Concept %d" % (i),
                linked_project_task = project_tasks[randint(0, len(project_tasks) - 1)],
                concept_definition = "Definition of Concept %d" % (i))
        building_blocks.add_building_block(concept)
    building_blocks.print_building_blocks()
    
    #[Step 3 - Test]
    tests = TestList()

    #[Step 3.0 - Test Definition]
    input("\nYou are about to begin [Test Definition].\nPress Enter key to continue...")
    print("\n[Test Definition]")
    executor_languages = ["Java", "Python", "C", "C++", "C#", "JavaScript"]
    parameters = ["x = 2", "y = 3", "z = 1", "k = -4", "l = [1, 0, 1]", "m = 0.33", "n = 1.39"]
    for block in building_blocks.items:
        if block.testable:
            if type(block) == Code:
                test_parameters = sample(parameters, randint(MIN_TEST_PARAMETERS, MAX_TEST_PARAMETERS))
                language = executor_languages[randint(0, len(executor_languages) - 1 )]
            else:
                test_parameters = []
                language = ""
            executor = Executor(
                code = block,
                language = language)
            test = Test(
                linked_building_block = block,
                executor = executor,
                test_parameters = test_parameters)
            tests.add_test(test)
    tests.print_tests()

    #[Step 3.1 - Tests Execution]
    while not READY_TO_DEPLOY:
        input("\nYou are about to begin [Test Execution].\nPress Enter key to continue...")
        print("\n[Test Execution]")
        for test in tests.items:
            test.test_building_block()
        tests.print_tests()
        if tests.all_tests_passed():
            READY_TO_DEPLOY = True
        else:
            print("\nIn order to proceed, all tests must be successfull!\n")

    #[Step 4 - Deploy]
    if READY_TO_DEPLOY:
        print("\nHence all tests have been successfull, the software can now be deployed!\n")
    else:
        print("\nHence at least one test haven't been successfull, the software can NOT be deployed!\n")

    input("Press Enter key to finish...")