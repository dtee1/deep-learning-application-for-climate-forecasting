import argparse
from climate_learn.data import download1
from typing import List

def download_data(years: List[str], dataset: str, variable: str, area: List[float], resolution: str, api_key: str, root_dir: str):
    for i, year in enumerate(years):
        download1(root=root_dir, source="copernicus", variable=variable, dataset=dataset, year=year, resolution=resolution, area=area, api_key=api_key)

def main(years: List[str], dataset: str, variable: str, area: List[float], resolution: str, api_key: str, root_dir: str):
    download_data(years, dataset, variable, area, resolution, api_key, root_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download climate data.')
    parser.add_argument('--years', nargs='+', help='List of years to download data for', default=[str(y) for y in range(1975, 2023)])
    parser.add_argument('--dataset', help='Climate dataset to download data from', required=True)
    parser.add_argument('--variable', help='Climate variable to download data for', required=True)
    parser.add_argument('--area', nargs='+', help='Area of interest for the data in latitude and longitude coordinates. Should be in the form of [lat_min, lon_min, lat_max, lon_max]', default=[58, -100, 42.5, -68.5])
    parser.add_argument('--resolution', help='Resolution of the data in degrees. Default is 0.25', default='0.25')
    parser.add_argument('--api_key', help='API key for accessing the climate data', required=True)
    parser.add_argument('--root_dir', help='Root directory to save the downloaded data', default='./')

    args = parser.parse_args()

    years = args.years
    dataset = args.dataset
    variable = args.variable
    area = [float(coord) for coord in args.area]
    resolution = args.resolution
    api_key = args.api_key
    root_dir = args.root_dir

    main(years, dataset, variable, area, resolution, api_key, root_dir)
