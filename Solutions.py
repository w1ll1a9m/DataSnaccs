#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:37:06 2022

@author: williamlopez
"""

from typing import List
from math import log10, ceil

class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        '''Given an integer x, return true if x is palindrome integer.
        Without converting the int to string'''

        #get number of digits
        
        if x>0:
            digits = int(log10(x)+1)
            check = True
        elif x ==0:
            digits = 1
            check = True
        else:
            digits = int(log10(-x)+1)
            check = False
        
        #now we extract the digits from the int
        the_digits = []
        num_0 = x
        z=0
        mid = ceil(digits/2)-1
        
        for i in range(digits-1, -1, -1):
        
            digit = num_0//10**i
            the_digits.append(digit)
            num_0 = num_0 - digit*(10**i)
            position = digits-1-i
            if i == mid:

                if the_digits[position] != the_digits[ mid]:
                    check=False
                    break
                z=z+1
                
            elif i < mid:
                if the_digits[position] != the_digits[ mid-z]:
                    check = False
                    break
                z=z+1
                       
        return check
    
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, 
        and you may not use the same element twice.
        You can return the answer in any order.'''
        
        target_list = [target-x for x in nums]
        lookup = {nums[i]: [] for i in range(0, len(nums))}
        
        for i in range(0,len(nums)):
            lookup[nums[i]].append(i)
            
        for i in range(len(nums)):
            hits = lookup.get(target_list[i],-1)
        
            if hits != -1:
                if i in hits: 
                    hits.remove(i)
                if len(hits)>0:
                    sol = [i]+hits
                    break           
        return sol
    

    
    def isValid(self, s: str) -> bool:
        
        '''Given a string s containing just the characters '
        (', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.'''
      
        stack =[]
        par = {'(':')', '{':'}', '[':']', '}':'', ')':'', ']':''}
        
        for char in s:

            #append char in the stack
            stack.append(char)
            #check if the char is closing its coresponding parenthesis
            if len(stack)>1:
                if char == par[stack[-2]] :
                    stack.pop()
                    stack.pop()
                    #remove from the stack

            return bool(stack)
        