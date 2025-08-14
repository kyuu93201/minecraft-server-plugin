import nbtlib

# Đường dẫn tới file level.dat
level_path = "oneblock/level.dat"

# Mở file NBT
nbtfile = nbtlib.load(level_path)

# Trong file level.dat, dữ liệu chính nằm ở key "Data"
data = nbtfile["Data"]

# In tọa độ spawn hiện tại
print("📍 Spawn hiện tại:", data["SpawnX"], data["SpawnY"], data["SpawnZ"])

# Đổi tọa độ spawn
data["SpawnX"] = nbtlib.Int(-10)
data["SpawnY"] = nbtlib.Int(61)
data["SpawnZ"] = nbtlib.Int(-16)

# Lưu lại
nbtfile.save()

print("✅ Đã đổi spawn point thành (-10, 61, -16)")
