import argparse

from hys_scraper import HYS_Scraper


def main():
    """Runs the 'Have your Say' parser with command line arguments."""
    parser = argparse.ArgumentParser(
        prog="python3 -m hys_scraper",
        description="Scrape feedback and statistics from the European Commission's "
        + "'Have your Say' plattform.",
    )
    parser.add_argument(
        "publication_id",
        metavar="PID",
        type=str,
        help="The publication id - what comes after 'p_id=' in the initiative's URL.",
    )
    parser.add_argument(
        "--dir",
        "--target_dir",
        metavar="target_dir",
        type=str,
        default=None,
        help="Directory to save the feedback and statistics dataframes to. "
        + "Defaults to creating a new folder in the current working directory.",
    )
    parser.add_argument(
        "--no_attachments",
        action="store_true",
        help="Whether to skip the download of attachments.",
    )
    parser.add_argument(
        "--sleep_time",
        metavar="t",
        type=int,
        default=None,
        help="Minimum time between consecutive HTTP requests (in seconds).",
    )

    # Deviate from scraper's default values only if user specified something
    args = parser.parse_args()
    kwargs = {}
    if args.dir is not None:
        kwargs["target_dir"] = args.dir
    if args.no_attachments:
        kwargs["download_attachments"] = False
    if args.sleep_time is not None:
        kwargs["sleep_time"] = args.sleep_time

    # Scrape using the user-set parameters
    HYS_Scraper(args.publication_id, **kwargs).scrape()


if __name__ == "__main__":
    main()
