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
