instrumental_variables = [
    "BPSYS",  # Systolic blood pressure [70,230]
    "CBSTROKE",  # epileptic seizure [0 1 2 9 -4] (infarctus du myocarde)
    "HYPERTEN",  # Hypertension[0 1 2 9 -4]
    "NACCCCBS",  # calcium channel blocker [0 1 -4]
    "NACCADC",  # ADC at which the patient was diagnosed
    "EPILEP",  # epileptic seizure [0 1 2 9 -4]
]
confounders = [
    "VISIT",
    "INDEPEND",  # Independence score 1 - 4
    "INLIVWTH",  # In-living with partner (binary)
    "NACCAC",  # anticoagulant [0 1 -4]
    "NACCBETA",  # Beta blocker [0 1 -4]
    "NACCADEP",  # antidepressant [0 1 -4]
    "NACCPDMD",  # antiparkinson agent [0 1 -4]
    "CVDCOG",  # Cerebrovascular disease contributing to cognitive impairment [0 1 8 -4]
    "NACCMOCA",  # MoCA Total Score — corrected for education
    "NACCMMSE",  # Mini-Mental State Examination
    "FAQ",  # Functional Activities Questionnaire
    "NACCGDS",  # Geriatric Depression Scale
    "CDRGLOB",  # Global CDR® -> used as the outcome
]
outcome_predictors = [
    "NACCNIHR",
    "SEX",
    "EDUC",
    "NACCBMI",
    "TBI",
    "NACCAPSY",  # antipsychotic [0 1 -4]
    "DEPOTHR",  # Past depression episodes
    "NACCFAM",  # Family member with cognitive impairment
    "NACCFFTD",  # Family FLTD mutation
    "MEDS",  # COG IMPAIRMENT DUE TO Medications
    "ALCDEM",  # Alcohol-related dementia
    "PD",  # Parkinson's disease diagnosis
    "ALSFIND",  # ALS suspicion
    "PTSD",  # Post-traumatic Stress Disorder (3 levels: 0, 1, 2)
    "BIPOLAR",  # Bipolar disorder (3 levels: 0, 1, 2)
    "SCHIZ",  # Schizophrenia (3 levels: 0, 1, 2)
    "ANXIETY",  # Anxiety (3 levels: 0, 1, 2)
    "ALCOHOL",  # Alcohol (3 levels: 0, 1, 2)
    "NPSYDEV",  # Developmental neuropsychiatric disorders (3 levels: 0, 1, 2)
    "DELIR",  # Delirium (binary)
    "PTSDDX",  # PTSD with depression (binary)
    "COGMODE",  # COG MODE OF ONSET (ordinal)
    "MOMODE",  # MO MODE OF ONSET (ordinal)
    "JUDGMENT",  # Judgment and problem-solvin (ordinal but has 0.5 status -> continuous)
    "CDRSUM",  # CDR® sum of boxes (score 0 - 18)
    "COMPORT",  # Behavior, comportment, and personality (ordinal but has 0.5 status -> continuous)
    "CDRLANG",  # Language (ordinal but has 0.5 status -> continuous)
    "DECCLIN",  # Clinician believes there is a meaningful decline in memory,
    # non-memory cognitive abilities, behavior, ability to manage his/her affairs,
    # or there are motor/movement changes (binary)
]