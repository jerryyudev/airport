import csv
from geopy.distance import geodesic

def load_airport_data(file_path):
    """
    从CSV文件中加载机场数据
    """
    airports = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            airport_code = row['iata_code']
            airport_name = row['name']
            latitude = float(row['latitude_deg'])
            longitude = float(row['longitude_deg'])
            airports[airport_code] = (latitude, longitude, airport_name)
    return airports

def get_distance(source_coords, destination_coords):
    """
    计算两个地点之间的距离
    """
    distance = geodesic(source_coords, destination_coords).kilometers
    return distance

def get_time_to_destination(distance, speed):
    """
    计算到达目的地所需时间
    """
    time_hours = distance / speed
    return time_hours

def main():
    # 加载机场数据
    airport_data = load_airport_data('airports.csv')

    # 用户输入源地点的经纬度
    source_lat = float(input("请输入您的纬度："))
    source_lon = float(input("请输入您的经度："))

    # 用户输入目标机场
    destination_code = input("请输入目标机场的三字代码：")

    # 获取目标机场的经纬度和名称
    destination_info = airport_data.get(destination_code)
    if destination_info is None:
        print("无法找到目标机场的坐标信息")
        return

    destination_coords = destination_info[:2]
    destination_name = destination_info[2]

    # 计算距离
    source_coords = (source_lat, source_lon)
    distance = get_distance(source_coords, destination_coords)
    print("您与目标机场（{}）的距离为：{:.2f} 公里".format(destination_name, distance))

    # 输出目标机场的坐标
    print("目标机场（{}）的坐标为：{}".format(destination_name, destination_coords))

    # 用户输入飞行速度
    speed = float(input("请输入飞机速度（公里/小时）："))

    # 计算到达目的地所需时间
    time_to_destination = get_time_to_destination(distance, speed)
    print("到达目的地（{}）所需时间为：{:.2f} 小时".format(destination_name, time_to_destination))

if __name__ == "__main__":
    main()
