from torch import nn
class LinearBlock(nn.Module):
def __init__(self, dim, mlp_ratio=4., drop=0., drop_path=0., act=nn.GELU,
norm=nn.LayerNorm, n_tokens=197): # 197 = 16**2 + 1
super().__init__()
self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()
# FF over features
self.mlp1 = Mlp(in_features=dim, hidden_features=int(dim*mlp_ratio), act=act, drop=drop)
self.norm1 = norm(dim)
# FF over patches
self.mlp2 = Mlp(in_features=n_tokens, hidden_features=int(n_tokens*mlp_ratio), act=act, drop=drop)
self.norm2 = norm(n_tokens)
def forward(self, x):
x = x + self.drop_path(self.mlp1(self.norm1(x)))
x = x.transpose(-2, -1)
x = x + self.drop_path(self.mlp2(self.norm2(x)))
x = x.transpose(-2, -1)
return x
class Mlp(nn.Module):
def __init__(self, in_features, hidden_features, act_layer=nn.GELU, drop=0.):
super().__init__()
self.fc1 = nn.Linear(in_features, hidden_features)
self.act = act_layer()
self.fc2 = nn.Linear(hidden_features, in_features)
self.drop = nn.Dropout(drop)
def forward(self, x):
x = self.fc1(x)
x = self.act(x)
x = self.drop(x)
x = self.fc2(x)
x = self.drop(x)
return x
