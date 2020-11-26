### Objective

Your assignment is to create a Pokémon API from a CSV file using Python and any framework.

### Brief

Professor Oak is in trouble! A wild Blastoise wreaked havoc in the server room and destroyed every single machine. There are no backups - everything is lost! Professor Oak quickly scribbles down all the Pokémon from memory and hands them to you on a piece of paper. (`/Data/pokemon.csv`). Your task is to restore the Pokémon Database from that file and create a Pokémon API so that they’re never lost again.

### Tasks

- [x] Implement assignment using:
  - [x] Language: **Python**
  - [x] Framework: **any framework**
- [x] Create a Pokémon Model that includes all fields outlined in `/Data/pokemon.csv`
- [x] Parse the .csv file and create entries for each row based on the following conditions:
  - [x] Exclude Legendary Pokémon
  - [x] Exclude Pokémon of Type: Ghost
  - [x] For Pokémon of Type: Steel, double their HP
  - [x] For Pokémon of Type: Fire, lower their Attack by 10%
  - [x] For Pokémon of Type: Bug & Flying, increase their Attack Speed by 10%
  - [x] For Pokémon that start with the letter **G**, add +5 Defense for every letter in their name (excluding **G**)
- [x] Create one API endpoint `/pokemons`
  - [x] This API endpoint should be searchable, filterable and paginatable
    - [x] Search: name
      - [x] Bonus: implement fuzzy search using Levenshtein distance
    - [x] Filter: HP, Attack & Defense
      - [x] `/pokemons?hp[gte]=100&defense[lte]=200`
    - [x] Pagination: e.g. `/pokemons?page=1`

### Evaluation Criteria

- **Python** best practices
- Show us your work through your commit history
- We're looking for you to produce working code, with enough room to demonstrate how to structure components in a small program
- Completeness: did you complete the features?
- Correctness: does the functionality act in sensible, thought-out ways?
- Maintainability: is it written in a clean, maintainable way?
- Testing: is the system adequately tested?

### CodeSubmit

Please organize, design, test and document your code as if it were going into production - then push your changes to the master branch. After you have pushed your code, you may submit the assignment on the assignment page.

All the best and happy coding,

The Qualio Team
