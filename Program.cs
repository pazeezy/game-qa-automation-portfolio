// 1. Define our expected values (variables)
string expectedBuildVersion = "v1.0.4-Release";
bool isServerOnline = true;

// 2. Define what the test actually found (simulating a test run)
string actualBuildVersion = "v1.0.3-Release";

Console.WriteLine("Starting automated smoke test...");

// 3. The actual QA check (Logic)
if (actualBuildVersion != expectedBuildVersion)
{
    Console.WriteLine($"FAIL: Build mismatch! Expected {expectedBuildVersion}, but got {actualBuildVersion}.");
}
else if (!isServerOnline)
{
    Console.WriteLine("FAIL: Build version is correct, but the game server is offline.");
}
else
{
    Console.WriteLine("PASS: Build version matches and server is online. Safe to proceed.");
}