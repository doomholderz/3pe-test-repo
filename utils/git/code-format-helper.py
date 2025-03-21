import argparse
import os
import subprocess
import sys

if __name__ == "__main__":
    print("running normally")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--token", type=str, required=True, help="GitHub authentiation token"
    )
    parser.add_argument(
        "--repo",
        type=str,
        default=os.getenv("GITHUB_REPOSITORY", "llvm/llvm-project"),
        help="",
    )
    parser.add_argument("--issue-number", type=int, required=True)
    parser.add_argument(
        "--start-rev",
        type=str,
        required=True,
        help="",
    )
    parser.add_argument(
        "--end-rev", type=str, required=True, help=""
    )
    parser.add_argument(
        "--changed-files",
        type=str,
        help="",
    )

    args = parser.parse_args()
    print("finished normally")

    sys.exit(1)