import express from "express";
import numberGeneratorController from "../controllers/numberGeneratorController";

const router = express.Router();

router.use("/random", numberGeneratorController);

export default router;