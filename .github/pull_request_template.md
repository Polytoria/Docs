---
name: Doc Improvement
about: You've made changes to the Polytoria documentation
title: "[ REPLACE this with a DETAILED SUMMARY of your changes ]"
labels: documentation
assignees: ''
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to contribute to the Polytoria documentation project!
        Please ensure that this PR meets the following criteria:
        - [ ] The changes you've made are accurate and correct
        - [ ] Distinct changes for separate issues are in separate PRs (do not combine multiple issues into one PR)
        - [ ] Any additions or modifications to example code were tested in the latest version of Polytoria Creator and work as intended
  - type: dropdown
    id: categories
    attributes:
      label: Select the category that best describes your changes (if your changes fit multiple categories, please split them into separate PRs)
      options:
        - This PR fixes a typo, grammatical error, or other typographical inaccuracy
        - This PR adds new documentation where none existed before
        - This PR improves existing documentation
        - This PR is a code example improvement
        - Other (please specify in the summary)
    validations:
      required: true
  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: Please provide a detailed summary of your changes.
      placeholder: Summary
    validations:
      required: true
---


