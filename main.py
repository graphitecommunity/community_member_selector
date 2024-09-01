import random
import pandas as pd

def select_community_member():
    community_members = pd.read_csv("community_member_details.csv")
    return random.choice(community_members["name"])

def main():
    print(f"The selected community member is: {select_community_member()}")

if __name__ == "__main__":
    main()