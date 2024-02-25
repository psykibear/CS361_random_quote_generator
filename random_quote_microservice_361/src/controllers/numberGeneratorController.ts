import express from "express";
import { RandomNumberGenerator } from "../models/numberGenerator";
import { Request, Response } from "express";

const router = express.Router();

// Return an integer between the given min and max query parameters
router.get("/range", async (req: Request, res: Response) => {
  const min = parseInt(req.query.min as string, 10);
  const max = parseInt(req.query.max as string, 10);

  if (!isNaN(min) && !isNaN(max)) {
    if (min > max) {
      res.status(400).json({ error: "Min should not be greater than Max" });
    } else {
      const randomNumber = RandomNumberGenerator.generate(min, max);
      res.json({ randomNumber });
    }
  } else {
    res.status(400).json({ error: "Bad Request" });
  }
});

// Return an integer between 1 and the given max integer parameter
router.get("/max/:maxInt", async (req: Request, res: Response) => {
  const maxInt = parseInt(req.params.maxInt, 10);

  if (!isNaN(maxInt)) {
    const randomNumber = RandomNumberGenerator.generate(1, maxInt);
    res.json({ randomNumber });
  } else {
    res.status(400).json({ error: "Bad Request" });
  }
});

export default router;
