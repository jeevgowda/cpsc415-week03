# Intent: Customer Inquiry Intent Classifier

## Purpose
A standard-library script that accepts user text inquiries, formats them for an LLM to produce structured JSON output classifying intent into predefined categories, and runs a 5-case evaluation matrix.

## Target Audience
Internal API router / automated support triage workflow.

## Core Commitments
1. The program must return structured JSON matching a strict schema (category, confidence, reasoning).
2. Valid categories: billing, technical_support, account_access, unknown.
3. Out-of-scope or unclassifiable inputs must return unknown.

## Approved by
Jeevan Gowda Kumaraswamy
Date: October 5, 2026
