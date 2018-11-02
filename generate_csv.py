#!/usr/bin/env python3
from faker import Faker
import csv
import random


fake = Faker("en_GB")

org_types = [
    "charity", 
    "mediation", 
    "private", 
    "solicitor"
]

categories = [
    "cat_actions_against_police",
    "cat_clinical_negligence",
    "cat_community_care",
    "cat_crime",
    "cat_debt",
    "cat_family",
    "cat_family_mediation",
    "cat_housing",
    "cat_immigration_or_asylum",
    "cat_mental_health",
    "cat_prison_law",
    "cat_public_law",
    "cat_welfare_benefits"
]

with open("legal-providers.csv", "w") as f:
    c = csv.writer(f, dialect="unix")

    c.writerow([
        "id",
        "name",
        "address1",
        "city",
        "postcode",
        "phone",
        "org_type",
    ] + categories)

    for i in range(100):
        c.writerow([
            i + 1,
            fake.company(),
            f"{fake.building_number()} {fake.street_name()}",
            fake.city(),
            fake.postcode(),
            fake.phone_number(),
            random.choice(org_types)
        ] + [random.choice([0, 1]) for c in categories])
