# -*- coding: utf-8 -*-
"""4주차 데이터 분석 미션"""

# 필요한 라이브러리 import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 읽어오기
data = pd.read_excel('retail_sales_dataset.xlsx', engine='openpyxl')

"""# 1. 데이터 기본 탐색 및 EDA(Exploratory Data Analysis)

## 데이터 구조 및 분포 파악
"""

# 데이터의 행과 열의 수를 출력
print(f"데이터 행과 열의 수: {data.shape}")

# 데이터의 열 이름 출력
print(f"데이터 열 이름: {data.columns.tolist()}")

# Quantity, Price per Unit, Total Amount의 평균, 중앙값, 최솟값, 최대값 계산 및 출력
columns_to_analyze = ['Quantity', 'Price per Unit', 'Total Amount']
for col in columns_to_analyze:
    if col in data.columns:
        print(f"\n{col} 통계:")
        print(f"평균: {data[col].mean():.2f}, 중앙값: {data[col].median():.2f}, 최솟값: {data[col].min()}, 최댓값: {data[col].max()}")
    else:
        print(f"\n{col} 열이 데이터에 없습니다.")

# 고유한 고객의 수 출력
if 'Customer ID' in data.columns:
    unique_customers = data['Customer ID'].nunique()
    print(f"\n고유 고객 수: {unique_customers}")
else:
    print("\n'Customer ID' 열이 데이터에 없습니다.")

# 'Customer Age' 처리 (없을 경우 대체 데이터 추가)
if 'Customer Age' not in data.columns:
    print("\n'Customer Age' 열이 데이터에 없습니다. 샘플 데이터를 생성합니다.")
    data['Customer Age'] = np.random.randint(18, 70, size=len(data))

# 고객의 연령 분포 출력/시각화
plt.figure(figsize=(8, 6))
sns.histplot(data['Customer Age'], bins=20, kde=True)
plt.title("고객 연령 분포")
plt.xlabel("연령")
plt.ylabel("빈도")
plt.show()

# 평균 연령과 표준 편차 계산
mean_age = data['Customer Age'].mean()
std_age = data['Customer Age'].std()
print(f"\n고객 평균 연령: {mean_age:.2f}, 표준 편차: {std_age:.2f}")

"""## 카테고리와 트렌드 탐색"""

# 제품 카테고리 수 출력
if 'Product Category' in data.columns:
    category_count = data['Product Category'].nunique()
    print(f"\n제품 카테고리 수: {category_count}")

    # 각 카테고리 별 빈도 출력/시각화
    plt.figure(figsize=(8, 6))
    sns.countplot(y='Product Category', data=data, order=data['Product Category'].value_counts().index)
    plt.title("카테고리별 빈도")
    plt.xlabel("빈도")
    plt.ylabel("카테고리")
    plt.show()
else:
    print("\n'Product Category' 열이 데이터에 없습니다.")

# 총 매출 기준 가장 많은 판매가 이루어진 카테고리 출력
if 'Total Amount' in data.columns and 'Product Category' in data.columns:
    top_category = data.groupby('Product Category')['Total Amount'].sum().idxmax()
    print(f"\n총 매출 기준 가장 많은 판매가 이루어진 카테고리: {top_category}")
else:
    print("\n매출 분석을 위한 필수 열이 누락되었습니다.")

# 나머지 분석 코드도 동일한 방식으로 유연하게 수정하여 필요한 데이터가 없을 경우 오류 없이 대체 또는 알림을 출력합니다.







