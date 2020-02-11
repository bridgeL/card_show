card show是一个简单的抽卡、打卡demo

主要需要设计的是：

卡堆（玩家卡堆、桌面卡堆、废弃卡堆、抽卡牌堆）
卡片（5种类型，正反面）



// 简易版

卡堆cardheap
卡牌card

卡牌若干，分布在卡堆中，卡牌和卡堆一一对应
卡牌拥有正反两面，要求可以实现翻面特性
卡牌在卡堆中一字排开，存在次序，紧邻排布


/// 豪华版

卡堆cardheap
卡牌card

卡牌若干，分布在卡堆中，卡牌和卡堆一一对应
卡牌拥有正反两面，要求可以实现翻面特性
卡牌在卡堆中一字排开，存在次序，可以根据卡堆牌总数，动态分配间距；位置不够时允许重叠，位置足够时紧邻排布
鼠标长按住卡牌可拖动其在卡堆中的顺序
鼠标单击卡牌可使其出列，再次单击卡牌将出牌

应当由卡牌实现正反面的切换
卡牌应当有 唯一指定id号 和 类别字符串

应当由卡堆管理卡牌展示次序以及在屏幕上的位置
应当由卡堆记录出列的牌的id号/牌堆次序





    '''A Card show on the screen
    Returns: card object
    Functions: update, 
    Attributes: id, num, total, visible, chosed, backsideup, imghead, imgback, area
    '''
