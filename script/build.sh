#!/bin/bash

#构建LAMC
function buildLAMC() {
    pyinstaller LAMC.spec -y
}

#构建升级工具
function buildUpgrade() {
    pyinstaller -F tools/upgrade/upgrade.py -y
    mv dist/upgrade dist/LAMC
    rm upgrade.spec
}

function main() {
    buildLAMC
    buildUpgrade
}

main