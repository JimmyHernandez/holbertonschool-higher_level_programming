#!/bin/bash
-- This script is to list all
-- records in the second_table

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
