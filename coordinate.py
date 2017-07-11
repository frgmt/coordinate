# -*- coding:utf-8 -*-

from math import modf


class Coordinate(object):

    def __init__(self, latitude, longitude):
        # dms
        if str(latitude).count('.') > 1 and str(longitude).count('.') > 1:
            latitude_list = str(latitude).split('.')
            self.__latitude = float(latitude_list[0]) + float(latitude_list[1]) / 60 + float('.'.join([latitude_list[2], latitude_list[3]])) / 3600
            longitude_list = str(longitude).split('.')
            self.__longitude = float(longitude_list[0]) + float(longitude_list[1]) / 60 + float('.'.join([longitude_list[2], longitude_list[3]])) / 3600
        # milli
        elif float(latitude) > 1000 and float(longitude) > 1000:
            self.__latitude = float(latitude) / 3600000
            self.__longitude = float(longitude) / 3600000
        # deg
        else:
            self.__latitude = float(latitude)
            self.__longitude = float(longitude)

    def get_deg_latitude(self):
        """
        度 表記 (Degree)
        :return: 緯度
        """
        return self.__latitude

    def get_deg_longitude(self):
        """
        度 表記 (Degree)
        :return: 経度
        """
        return self.__longitude

    def get_dms_latitude(self):
        """
        度/分/秒 表記 (Degree Minute Second)
        :return: 緯度
        """
        decimal, degree = modf(self.__latitude)
        second, minute = modf(decimal * 60)
        return '.'.join([str(int(degree)), str(int(minute)), str(second * 60)])

    def get_dms_longitude(self):
        """
        度/分/秒 表記 (Degree Minute Second)
        :return: 経度
        """
        decimal, degree = modf(self.__longitude)
        second, minute = modf(decimal * 60)
        return '.'.join([str(int(degree)), str(int(minute)), str(second * 60)])

    def get_milli_latitude(self):
        """
        ミリ秒 表記
        :return: 緯度
        """
        return self.__latitude * 3600000

    def get_milli_longitude(self):
        """
        ミリ秒 表記
        :return: 経度
        """
        return self.__longitude * 3600000

    def tokyo_to_wgs84(self):
        """
        日本測地系から世界測地系へ変換
        """
        self.__latitude = self.__latitude - self.__latitude * 0.00010695 + self.__longitude * 0.000017464 + 0.0046017
        self.__longitude = self.__longitude - self.__latitude * 0.000046038 - self.__longitude * 0.000083043 + 0.010040

    def wgs84_to_tokyo(self):
        """
        世界測地系から日本測地系へ変換
        """
        self.__latitude = self.__latitude + self.__latitude * 0.00010696 - self.__longitude * 0.000017467 - 0.0046020
        self.__longitude = self.__longitude + self.__latitude * 0.000046047 + self.__longitude * 0.000083049 - 0.010041
