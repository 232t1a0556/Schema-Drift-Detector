Test Case 1: Add New Column
Test Case ID : TC_01
Scenario:Add a new column
Initial Schema:id, name, salary
Modified Schema:id, name, salary, department
Expected Result:System detects "department" as added column
Risk Level:LOW
Status:Pass

Test Case 2: Remove Existing Column
Test Case ID :TC_02
Scenario:Remove salary column
Initial Schema:id, name, salary
Modified Schema:id, name
Expected Result:System detects removed column
Risk Level:HIGH
Status:Pass


Test Case 3: Change Data Type
Test Case ID
TC_03
Scenario
Change salary REAL to TEXT
Expected Result
Detect datatype change
Risk Level
MEDIUM
Status
Pass
Test Case 4: Add Multiple Columns

Test Case ID: TC_04

Scenario: Add columns department and email

Expected Result: Detect both added columns

Risk Level: LOW

Status: Pass

Test Case 5: Add New Table

Test Case ID: TC_05

Scenario: Add new table projects

Expected Result: Detect newly added table

Risk Level: LOW

Status: Pass

Test Case 6: Remove Table

Test Case ID: TC_06

Scenario: Delete table departments

Expected Result: Detect removed table

Risk Level: HIGH

Status: Pass

Test Case 7: No Schema Change

Test Case ID: TC_07

Scenario: Compare identical schemas

Expected Result: No schema drift detected

Risk Level: NONE

Status: Pass

Test Case 8: Rename Column

Test Case ID: TC_08

Scenario: Rename salary to employee_salary

Expected Result: Detect old column removed and new column added

Risk Level: MEDIUM

Status: Pass

Test Case 9: Add Primary Key

Test Case ID: TC_09

Scenario: Add PRIMARY KEY constraint to a column

Expected Result: Detect primary key addition

Risk Level: HIGH

Status: Pass

Test Case 10: Remove Primary Key

Test Case ID: TC_10

Scenario: Remove PRIMARY KEY constraint

Expected Result: Detect primary key removal

Risk Level: HIGH

Status: Pass

Test Case 11: Add NOT NULL Constraint

Test Case ID: TC_11

Scenario: Add NOT NULL constraint to a column

Expected Result: Detect constraint addition

Risk Level: MEDIUM

Status: Pass

Test Case 12: Remove NOT NULL Constraint

Test Case ID: TC_12

Scenario: Remove NOT NULL constraint from a column

Expected Result: Detect constraint removal

Risk Level: LOW

Status: Pass

Test Case 13: Add Foreign Key

Test Case ID: TC_13

Scenario: Add FOREIGN KEY relationship

Expected Result: Detect foreign key addition

Risk Level: MEDIUM

Status: Pass
