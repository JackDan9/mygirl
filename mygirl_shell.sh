#!/bin/bash
# Author: JackDan
# Date: 2018-09-04
# ****** Description ******
# The script is used to run scrapy projects(mygirl, mygirlJoke) 
# ************************

venv_path="/home/jackdan/py2env/bin"
mygirl_path="/home/jackdan/mygirl_html/mygirl/mygirl/spiders"
mygirlJoke_english_path="/home/jackdan/mygirlJoke/mygirlJoke/spiders"

# basepath=$(cd `dirname $0`; pwd)

main() {
    if [[ ! -d ${venv_path} ]]; then
        echo "*****please intall python virtualenv in ${venv_path}****"
    else 
        echo "*****${venv_path} is already exits*****"
        cd ${venv_path}
        pwd
        source activate
        
        if [[ ! -d ${mygirl_path} ]]; then
            echo "*****please install mygirl project in ${mygirl_path}*****"
        else
            cd ${mygirl_path}
            pwd
            scrapy crawl mygirl 
        fi

        
        if [[ ! -d ${mygirlJoke_english_path} ]]; then
            echo "*****please install mygirl project in ${mygirlJoke_english_path}*****"
        else
            cd ${mygirlJoke_english_path}
            pwd
            scrapy crawl mygirlJoke
        fi
    fi
}

main


