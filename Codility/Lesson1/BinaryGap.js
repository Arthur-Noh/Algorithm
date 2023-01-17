const solution = (N) => {
    const binaryNumber = N.toString(2);
    const gapNote = [];
    let maxGapCount = 0;

    binaryNumber.split('').map(value => {
        if (value == 1) {
            gapNote.push(maxGapCount);
            maxGapCount = 0;
        } else {
            maxGapCount++;
        }
    });

    return Math.max(...gapNote);
};
