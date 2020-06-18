#!/bin/bash

function create-repo(){

     read -p "Github Username: " username
     read -s -p "Github Password: " password
     python3 github_automate.py $1 username password
}