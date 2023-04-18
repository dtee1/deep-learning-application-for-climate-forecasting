import argparse
from climate_learn.data import download1
from typing import List

def download_data(years: List[str], dataset: str, variable: str, area: List[float], resolution: str, api_key: str, root_dir: str):
    for i, year in enumerate(years):
        download1(root=root_dir, source="copernicus", variable=variable, dataset=dataset, year=year, resolution=resolution, area=area, api_key=api_key)

def main(years_list: List[int], area: List[float], dataset: str, variable: str, resolution: str, api_key: str, root_dir: str):
    years = [str(year) for year in years_list] # convert the years to strings
    download_data(years, dataset, variable, area, resolution, api_key, root_dir)

    if len(years_list) == 1:
        year_arg = str(years_list[0])
    else:
        year_arg = f"{years_list[0]}/{years_list[-1]}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download climate data.')
    parser.add_argument('--years', nargs='+', help='List of years to download data for', default=['1990', '2023'])
    parser.add_argument('--dataset', help='Climate dataset to download data from', required=True)
    parser.add_argument('--variable', help='Climate variable to download data for', required=True)
    parser.add_argument('--area', nargs='+', type=float, help='Area of interest for the data in latitude and longitude coordinates. Should be in the form of [lat_min, lon_min, lat_max, lon_max]', default=[42.0, -81.0, 45.0, -78.0])
    parser.add_argument('--resolution', help='Resolution of the data in degrees. Default is 0.25', default='0.25')
    parser.add_argument('--api_key', help='API key for accessing the climate data', required=True)
    parser.add_argument('--root_dir', help='Root directory to save the downloaded data', default='/content/drive/MyDrive/Climate/.climate_tutorial')

    args = parser.parse_args()

    main(args.years, args.area, args.dataset, args.variable, args.resolution, args.api_key, args.root_dir)

