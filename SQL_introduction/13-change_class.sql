#!/bin/bash
-- This script is to list all
-- records in the second_table

DELETE FROM second_table WHERE score <= 5 ORDER BY score DESC;

