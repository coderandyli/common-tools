import matplotlib.pyplot as plt

# 生成曲线图
def generate_chart(x, y):
    # 配置-警戒线
    plt.axhline(y=100, color='red', linewidth=0.7)

    # 绘制曲线图
    plt.plot(x, y)

    # 添加标题和标签
    plt.title("Liang Han's mood swings")
    plt.xlabel("Time")
    plt.ylabel("Mood value")

    # 导出图表为PNG文件
    plt.savefig('line_plot.png')

    # 显示图表
    # plt.show() 与 plt.savefig()不能同时使用
    plt.show()


if __name__ == "__main__":

    # 准备数据
    x = ['unborn', '2024-06-05', '2024-06-06 07:00', 'now']
    y = [100, 100, 100 + 30 + 50 + 10, 100]

    # 生成折线图
    generate_chart(x, y)
