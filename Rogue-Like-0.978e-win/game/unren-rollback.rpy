init 999 python:
  renpy.config.rollback_enabled = True
  renpy.config.hard_rollback_limit = 256
  renpy.config.rollback_length = 256
  def unren_noblock():
    return
  renpy.block_rollback = unren_noblock
