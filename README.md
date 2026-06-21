# password-strength-checker
# Password Strength Checker

A Python tool that evaluates password strength using multiple security factors.

## What It Checks

- **Length** — minimum 8 characters
- **Uppercase letters** — at least one
- **Lowercase letters** — at least one
- **Digits** — at least one
- **Symbols** — special characters like !@#$%
- **Repeated characters** — flags lazy patterns like "aaa" or "111"
- **Common passwords** — checks against a list of frequently breached passwords

## How It Works

The program takes a password as input, scans each character to detect 
character type variety, then calculates a score out of 6. Based on the 
score, it gives a verdict: STRONG, MODERATE, or WEAK. If the password 
matches a known commonly-used password, it immediately flags it as 
dangerous regardless of score.

## Example

Input: `Hello123_`
Output: `STRONG password!`

Input: `password123`
Output: `DANGER: This is a commonly used, easily hacked password!`

## Why I Built This

I built this while preparing for IIT Kanpur's B.Cyber. program, applying 
concepts from Harvard's CS50 Cybersecurity course on securing data. This 
was my first real Python project, built and debugged independently to 
understand practical password security concepts.

## Tech Used
