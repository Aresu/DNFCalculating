from math import *
from PublicReference.base import *

#技能后的倍率是魔化后的倍率

class 复仇者主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '镰刀':
            return round(self.CD / self.恢复 * 0.95, 1)

class 复仇者技能0(复仇者主动技能):
    名称 = '恶魔之手'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 1148.298 * 2.24
    成长 = 129.7071 * 2.24
    CD = 5.7 * 1.6
    TP成长 = 0.08
    TP上限 = 5

class 复仇者技能1(复仇者主动技能):
    名称 = '死亡切割'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1029.22 * 2.25 * 1.163
    成长 = 115.7561 * 2.25 * 1.163
    CD = 4.8 * 1.6
    TP成长 = 0.1
    TP上限 = 5

class 复仇者技能2(被动技能):
    名称 = '镰刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 复仇者技能3(复仇者主动技能):
    名称 = '裂地锤'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 395.4524 * 2
    成长 = 45.55 * 2
    攻击次数 = 4
    #默认6hit，最高8hit,根据怪物体积,3觉后变更为范围攻击
    CD =4.8 * 1.55
    TP成长 = 0.10
    TP上限 = 5

class 复仇者技能4(被动技能):
    名称 = '恶魔诅咒'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能', '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割','永堕：混沌弑神','审判','魔流光杀','崩坏福音']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.03 * self.等级, 5)

class 复仇者技能5(复仇者主动技能):
    名称 = '回旋飞镰'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 586 * 1.9 * 1.05
    成长 = 56 * 1.9
    攻击次数 = 3
    基础2 = 337 * 1.9 * 1.05
    成长2 = 40 * 1.9 * 1.05
    攻击次数2 = 4
    CD = 8.0 * 1.5
    TP成长 = 0.10
    TP上限 = 5

class 复仇者技能6(复仇者主动技能):
    名称 = '复仇之刺'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5304.946 * 1.05 * 1.165
    成长 = 599.06 * 1.05 * 1.165
    CD = 9.5 * 1.6
    TP成长 = 0.10
    TP上限 = 5

class 复仇者技能7(复仇者主动技能):
    名称 = '厄运之轮'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 36
    基础 = 7454.839 * 1.165
    成长 = 842.8011 * 1.165
    CD = 15.2 * 1.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.25
        self.成长 *= 1.25

class 复仇者技能8(复仇者主动技能):
    名称 = '恶魔之拳'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7231.594 * 1.128
    成长 = 817.4063 * 1.128
    CD = 19
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.25
        self.成长 *= 1.25
        self.CD *= 0.85

class 复仇者技能9(复仇者主动技能):
    名称 = '恶魔之握'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9724.781 * 1.099
    成长 = 1098.22 * 1.099
    CD = 28.5
    TP成长 = 0.10
    TP上限 = 5

class 复仇者技能10(复仇者主动技能):
    名称 = '黑暗权能'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 31
    基础 = 458.23333 * 1.225
    成长 = 51.76666 * 1.225
    基础2 = 272.2666 * 1.225
    成长2 = 30.73333 * 1.225
    攻击次数2 = 32
    基础3 = 4803 * 1.225
    成长3 = 471.5161 * 1.225
    攻击次数3 = 1
    CD = 38
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.攻击次数2 = 42
        self.CD *= 0.9

class 复仇者技能11(复仇者主动技能):
    名称 = '魔化：末日审判者'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 7676 * 1.05
    成长 = 1714 * 1.05
    CD = 1
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.15


class 复仇者技能12(复仇者主动技能):
    名称 = '审判'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    基础 = 23921 * 1.1 * 1.095
    成长 = 7159 * 1.1 * 1.095
    CD = 145

class 复仇者技能13(被动技能):
    名称 = '恶魔唤醒'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['不朽战吼','地狱之门','厄运之轮','恶魔之拳','恶魔之手','恶魔之握','复仇之刺','黑暗权能','回旋飞镰','毁灭强击','裂地锤','末日浩劫','死亡切割','永堕：混沌弑神','魔流光杀','崩坏福音']
    关联技能2 = ['魔化：末日审判者']
    关联技能3 = ['审判']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.015 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.01 * self.等级, 5)

    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 复仇者技能14(复仇者主动技能):
    名称 = '地狱之门'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 1197 * 1.5 * 1.101
    成长 = 135 * 1.5 * 1.101
    攻击次数 = 8
    CD = 28.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.攻击次数 = 9

class 复仇者技能15(复仇者主动技能):
    名称 = '末日浩劫'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 16825.29 * 1.35 * 1.101
    成长 = 1899.706 * 1.35 * 1.101
    CD = 47.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    def 装备护石(self):
        self.基础 *= 1.18
        self.成长 *= 1.18

class 复仇者技能16(复仇者主动技能):
    名称 = '不朽战吼'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 6079.333 * 1.138
    成长 = 686.666 * 1.138
    攻击次数 = 5
    基础2 = 2172.6 * 1.138
    成长2 = 245.4 * 1.138
    攻击次数2 = 2
    CD = 38

class 复仇者技能17(被动技能):
    名称 = '原罪之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)

class 复仇者技能18(复仇者主动技能):
    名称 = '毁灭强击'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 40391.33 * 1.166
    成长 = 4562.325 * 1.166
    CD = 45.0

class 复仇者技能19(复仇者主动技能):
    名称 = '永堕：混沌弑神'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 83560.35 * 1.145
    成长 = 25256.53 * 1.145
    CD = 180.0

class 复仇者技能20(被动技能):
    名称 = '不死恶魔'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 复仇者技能21(复仇者主动技能):
    名称 = '魔流光杀'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 7562.4 * 1.2 * 1.3
    成长 = 853.6 * 1.2 * 1.3
    攻击次数 = 3
    基础2 = 34029 * 1.2 * 1.3
    成长2 = 3842 * 1.2 * 1.3
    攻击次数2 = 1
    CD = 40.0

class 复仇者技能22(复仇者主动技能):
    名称 = '崩坏福音'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 189029 * 1.4
    成长 = 57067 * 1.4
    CD = 180.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0

复仇者技能列表 = []
i = 0
while i >= 0:
    try:
        exec('复仇者技能列表.append(复仇者技能'+str(i)+'())')
        i += 1
    except:
        i = -1

复仇者技能序号 = dict()
for i in range(len(复仇者技能列表)):
    复仇者技能序号[复仇者技能列表[i].名称] = i

复仇者一觉序号 = 12
复仇者二觉序号 = 19
复仇者三觉序号 = 22

复仇者护石选项 = ['无']
for i in 复仇者技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        复仇者护石选项.append(i.名称)

复仇者符文选项 = ['无']
for i in 复仇者技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        复仇者符文选项.append(i.名称)

class 复仇者角色属性(角色属性):

    职业名称 = '复仇者'

    武器选项 = ['镰刀']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 1.90
   
    #基础属性(含唤醒)
    基础力量 = 793.0
    基础智力 = 952.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0

    def __init__(self):
        self.技能栏= deepcopy(复仇者技能列表)
        self.技能序号= deepcopy(复仇者技能序号)


    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['审判']].等级 = self.技能栏[self.技能序号['魔化：末日审判者']].等级


class 复仇者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 复仇者角色属性()
        self.角色属性A = 复仇者角色属性()
        self.角色属性B = 复仇者角色属性()
        self.一觉序号 = 复仇者一觉序号
        self.二觉序号 = 复仇者二觉序号
        self.三觉序号 = 复仇者三觉序号
        self.护石选项 = deepcopy(复仇者护石选项)
        self.符文选项 = deepcopy(复仇者符文选项)









