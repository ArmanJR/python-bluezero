from bluezero import broadcaster


def main():
    alt = broadcaster.Beacon()
    alt.add_manufacturer_data(
        '5558',  # Manufacturer ID (0xffff = Not for production)
        bytes.fromhex('18F90849B2CE2C5A7AD4D1494B757CDB7F10111213141516171819')
    )

    alt.start_beacon()


if __name__ == '__main__':
    main()
