judge = {
    "question": "question: Is\" The writer of the song Everyday America is a member of the duo Sugarland, not Roger Taylor\" true or false? think step by step and logically and give an \"True\" or \"False\" answer at the end of the answer.",
    "process": [
      "Song \"Everyday America\"",
      "Members of Sugarland",
      "Writers of \"Everyday America\"",
      "Roger Taylor"
    ],
    "judge": "True",
    "database_supporting_facts": [
      [
        "Jennifer Nettles",
        1
      ],
      [
        "Jennifer Nettles",
        2
      ],
      [
        "Roger Taylor (Queen drummer)",
        3
      ],
      [
        "Everyday America",
        4
      ]
    ],
    "fit": 0
  }

fit = 0
for j in judge['database_supporting_facts']:
    print (j[0])
    print (p for p in judge['process'])
judge['fit'] = fit    
