const path = require('path')
const fs = require('fs')

const readFile = (filename) => {
    if (fs.existsSync(path.join(__dirname, filename))) {
        const file = fs.readFileSync(path.join(__dirname, filename), 'utf-8')
        return file.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "").trim().split(" ");
    }
    throw new Error(`File ${filename} cannot be found.`)
}

const countFrequency = (wordsList) => {
    const D = {}
    for (word of wordsList) {
        if (word in D) {
            D[word] += 1
        } else {
            D[word] = 1
        }
    }
    return D
}

const getWordFrequencies = (filename) => {
    const wordsList = readFile(filename)
    return countFrequency(wordsList)
}

const innerProduct = (D1, D2) => {
    let sum = 0
    for (key in D1) {
        if (key in D2) {
            sum += D1[key] * D2[key]
        }
    }
    return sum
}

const vectorAngle = (D1, D2) => {
    numerator = innerProduct(D1, D2)
    denominator = Math.sqrt(innerProduct(D1, D1) * innerProduct(D2, D2))
    return Math.acos(numerator/denominator)
}


const main = () => {
    if (process.argv.length != 4) {
        console.log(`Usage: node document_distance.js filename1 filename2`)
    }

    const D1 = getWordFrequencies(process.argv[2])
    const D2 = getWordFrequencies(process.argv[3])
    const distance = vectorAngle(D1, D2)
    console.log(`The distance between document1 and document2: ${distance} radians.`)
}

main()