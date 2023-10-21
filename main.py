# This entrypoint file to be used in development. Start by reading README.md

from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 + 2", "45 + 43", "123 + 15"]
answer = arithmetic_arranger(problems)
print(answer)

