from datetime import date

TODAY = str(date.today())

qotd = {
    "id": TODAY,
    "title": "Two Sum",
    "difficulty": "Easy",
    "problem_statement": "...",

    "function_signature": "two_sum(nums, target)",

    "test_cases": [
        {
            "input": {"nums": [2,7,11,15], "target": 9},
            "output": [0,1]
        },
        {
            "input": {"nums": [3,2,4], "target": 6},
            "output": [1,2]
        }
    ],
    "hints": [
        "Use a hash map",
        "Trade space for time"
    ]
}


submissions = []
