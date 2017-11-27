#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2017/11/26

"""
    创建飞机
    在pygame中, 所有可移动的对象均叫可看作一个精灵(sprite)
    该类并实现了碰撞方法 spritecollide

    我方飞机和敌方飞机指定掩膜属性以及生存状态标志位 添加 self.mask 属性
"""

# 倒入精灵模块, 使飞机可以动起来
import pygame


class OurPlane(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        super(OurPlane, self).__init__()
        # 确定我方飞机背景图
        self.image_one = pygame.image.load("material/image/hero1.png")
        self.image_two = pygame.image.load("material/image/hero2.png")
        # 获取我方飞机的位置
        self.rect = self.image_one.get_rect()
        # 本地化背景图片的尺寸
        self.width, self.height = bg_size[0], bg_size[1]
        # 获取飞机图像的掩膜用以更加精确的碰撞检测
        self.mask = pygame.mask.from_surface(self.image_one)
        # 定义飞机初始化位置，底部预留60像素
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # 设置飞机移动速度
        self.speed = 10
        # 设置飞机存活状态(True为存活, False为死亡)
        self.active = True
        # 加载飞机损毁图片
        self.destroy_images = []
        self.destroy_images.extend(
            [
                pygame.image.load("material/image/hero_blowup_n1.png"),
                pygame.image.load("material/image/hero_blowup_n2.png"),
                pygame.image.load("material/image/hero_blowup_n3.png"),
                pygame.image.load("material/image/hero_blowup_n4.png")
            ]
        )

    def move_up(self):
        """
        飞机向上移动的操作函数，其余移动函数方法类似
        """
        if self.rect.top > 0:  # 如果飞机尚未移动出背景区域
            self.rect.top -= self.speed
        else:  # 若即将移动出背景区域，则及时纠正为背景边缘位置
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def move_left(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        # 初始化飞机
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        self.active = True










