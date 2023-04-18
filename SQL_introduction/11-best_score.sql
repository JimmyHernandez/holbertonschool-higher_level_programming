#!/bin/bash
-- This script is to list all
-- records in the second_table

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

