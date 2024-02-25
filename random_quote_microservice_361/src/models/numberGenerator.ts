export class RandomNumberGenerator {
    /**
     * Generates a random number within a specified range.
     * @param min The minimum value of the range (inclusive), defaulting to 0.
     * @param max The maximum value of the range (inclusive).
     * @returns A random number within the specified range.
     */
    static generate = (min = 0, max = 20) => Math.floor(Math.random() * (max - min + 1)) + min;
}
