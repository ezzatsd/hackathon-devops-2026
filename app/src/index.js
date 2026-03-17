require("./tracing");

const express = require("express");
const { Pool } = require("pg");

const app = express();
const port = process.env.PORT || 3000;

const pool = new Pool({
  host: process.env.DB_HOST || "localhost",
  port: Number(process.env.DB_PORT || 5432),
  user: process.env.DB_USER || "postgres",
  password: process.env.DB_PASSWORD || "postgres",
  database: process.env.DB_NAME || "appdb",
});

app.use(express.json());

app.get("/", async (_req, res) => {
  res.json({
    message: "Hackathon DevOps 2026",
    status: "running",
    observability: "enabled",
  });
});

app.get("/health", async (_req, res) => {
  try {
    await pool.query("SELECT 1");
    res.json({ status: "ok", database: "reachable" });
  } catch (error) {
    console.error("Health check failed:", error.message);
    res.status(500).json({
      status: "error",
      database: "unreachable",
      reason: error.message,
    });
  }
});

app.get("/users", async (_req, res) => {
  try {
    const result = await pool.query(
      "SELECT id, email, created_at FROM users ORDER BY id ASC",
    );

    res.json({
      count: result.rows.length,
      items: result.rows,
    });
  } catch (error) {
    console.error("Users endpoint failed:", error.message);
    res.status(500).json({
      error: "database_query_failed",
      message: error.message,
    });
  }
});

app.listen(port, () => {
  console.log(`Application running on port ${port}`);
});
