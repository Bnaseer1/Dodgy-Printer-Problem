import math, os, random, re, sys
from typing import List

def max_printable_documents(documents: List[int], is_malfunctioning: List[bool], x: int) -> int:
    failed_documents = []
    successful_documents = []
    successful_failed_documents = []
    result = 0

    for i in range (0, len(documents)):
        if is_malfunctioning[i] == True:
            failed_documents.append(documents[i])
        else:
            successful_documents.append(documents[i])

    failed_documents.sort(reverse=True)
    print(successful_documents)
    print(failed_documents)

    if x > len(failed_documents):
        y = len(failed_documents)
    else:
        y = x
    
    for i in range(0, y):
        successful_failed_documents.append(failed_documents[i])

    for num in successful_documents:
        result += num

    for num in successful_failed_documents:
        result += num

    return result

print(max_printable_documents([1000, 560, 8000, 23451, 55511, 23123, 55576, 1231230, 50432], [False, False, True, True, False, False, True, False, True, False], 10))
