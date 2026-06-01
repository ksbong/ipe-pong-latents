import argparse
from src.ipe_pong.data import load_metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata", required=True)
    args = parser.parse_args()

    df = load_metadata(args.metadata)

    print("shape:", df.shape)
    print("\ncolumns:")
    print(df.columns.tolist())

    print("\nhead:")
    print(df.head())

    useful_cols = [
        "x0", "y0", "dx", "dy", "speed0", "heading0",
        "t_occ", "t_f", "y_occ_hum", "y_f_hum",
        "x_occ_hum", "x_f_hum", "n_bounce",
        "n_bounce_correct",
    ]

    existing = [c for c in useful_cols if c in df.columns]
    print("\nuseful columns found:")
    print(existing)

    if existing:
        print("\nsummary:")
        print(df[existing].describe())


if __name__ == "__main__":
    main()