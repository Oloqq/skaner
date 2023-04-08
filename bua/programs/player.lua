local Object = require("classic")

local Player = Object:extend()

function Player:new(x, y)
  self.x = x
  self.y = y
end

function Player:update(dt)
  self.x = self.x + 1
end

function Player:draw()
  love.graphics.rectangle("fill", self.x, self.y, 10, 10)
end

return Player
