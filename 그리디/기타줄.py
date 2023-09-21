import sys
input = sys.stdin.readline

n, m = map(int, input().split())
package_min = 1000
normal_min = 1000
for _ in range(m):
    package, normal = map(int, input().split())
    package_min = min(package_min, package)
    normal_min = min(normal_min, normal)
result = min(package_min*(n//6)+normal_min*(n%6), package_min*(n//6+1), normal_min*n)
print(result)

