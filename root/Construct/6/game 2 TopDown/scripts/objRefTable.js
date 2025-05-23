const C3 = self.C3;
self.C3_GetObjectRefTable = function () {
	return [
		C3.Plugins.Tilemap,
		C3.Behaviors.solid,
		C3.Plugins.Sprite,
		C3.Behaviors.EightDir,
		C3.Behaviors.scrollto,
		C3.Plugins.Keyboard,
		C3.Plugins.Mouse,
		C3.Behaviors.Bullet,
		C3.Behaviors.Pin,
		C3.Behaviors.LOS,
		C3.Plugins.Audio,
		C3.Plugins.Button,
		C3.Plugins.TiledBg,
		C3.Plugins.Shape3D,
		C3.Plugins.System.Cnds.IsGroupActive,
		C3.Plugins.Keyboard.Cnds.IsKeyDown,
		C3.Behaviors.EightDir.Acts.SimulateControl,
		C3.Plugins.Sprite.Acts.SetMirrored,
		C3.Plugins.Sprite.Cnds.OnCollision,
		C3.Plugins.Sprite.Acts.SetAnim,
		C3.Behaviors.EightDir.Acts.SetMaxSpeed,
		C3.Plugins.Keyboard.Cnds.OnKey,
		C3.Plugins.Sprite.Acts.SetX,
		C3.Plugins.Sprite.Acts.SetY,
		C3.Plugins.System.Cnds.EveryTick,
		C3.Plugins.Mouse.Exps.Y,
		C3.Plugins.Mouse.Exps.X,
		C3.Plugins.Sprite.Acts.RotateTowardPosition,
		C3.Plugins.Sprite.Acts.SetTowardPosition,
		C3.Plugins.Mouse.Cnds.OnClick,
		C3.Plugins.Sprite.Acts.Spawn,
		C3.Plugins.System.Acts.Wait,
		C3.Plugins.Sprite.Acts.Destroy,
		C3.Plugins.System.Cnds.OnLayoutStart,
		C3.Behaviors.Pin.Acts.PinByImagePoint,
		C3.Plugins.Sprite.Cnds.IsBetweenAngles,
		C3.Plugins.Sprite.Acts.SetFlipped,
		C3.Plugins.Sprite.Cnds.CompareInstanceVar,
		C3.Plugins.Sprite.Acts.SubInstanceVar,
		C3.Plugins.Sprite.Acts.SetAnimFrame,
		C3.Plugins.Sprite.Acts.SetAngle,
		C3.Plugins.Sprite.Acts.MoveAtAngle,
		C3.Plugins.Sprite.Exps.X,
		C3.Plugins.Sprite.Exps.Y,
		C3.Behaviors.LOS.Cnds.HasLOSToObject,
		C3.Plugins.Sprite.Cnds.CompareX,
		C3.Plugins.Sprite.Cnds.CompareY,
		C3.Plugins.Audio.Acts.Play,
		C3.Plugins.System.Acts.ResetGlobals,
		C3.Plugins.System.Acts.RestartLayout,
		C3.Plugins.System.Cnds.Every,
		C3.Plugins.Sprite.Cnds.OnDestroyed,
		C3.Plugins.Button.Cnds.OnClicked,
		C3.Plugins.System.Acts.GoToLayout
	];
};
self.C3_JsPropNameTable = [
	{Solid: 0},
	{Стіна: 0},
	{Підлога: 0},
	{"8Direction": 0},
	{Стеження: 0},
	{RoboCat: 0},
	{Keyboard: 0},
	{камера: 0},
	{Миша: 0},
	{Приціл: 0},
	{Куля: 0},
	{Пуля: 0},
	{Прикріплення: 0},
	{Зброя: 0},
	{HP: 0},
	{ТвердеТіло: 0},
	{Колючка: 0},
	{хп: 0},
	{Привид: 0},
	{привидХП: 0},
	{XP: 0},
	{Змінна1: 0},
	{"8напрямків": 0},
	{ПолеЗору: 0},
	{"бабай💀👺": 0},
	{Спрайт: 0},
	{Спрайт2: 0},
	{Аудіо: 0},
	{Спрайт3: 0},
	{ХП: 0},
	{Спрайт4: 0},
	{F3F3F3F3F_3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F: 0},
	{maska_golova_minecraft_kriper_karton_: 0},
	{deepdarkcaves: 0},
	{tmb_356066_: 0},
	{F3F3F3F3F3F3F3F3F_3F3F3F3F3F: 0},
	{Sculk_Shrieker_BE: 0},
	{Deepslate_Tiles_JE: 0},
	{Polished_Deepslate_28texture29_JE: 0},
	{Deepslate_Tiles_28texture29_JE: 0},
	{СТРЕЛА: 0},
	{Basalt_28side_texture29_JE1_BE: 0},
	{Спрайт5: 0},
	{Спрайт6: 0},
	{Спрайт7: 0},
	{F3F3F3F3F3F3F3F3F3F3F_3F3F3F3F3F3F: 0},
	{Спрайт8: 0},
	{Спрайт9: 0},
	{F3F3F3F3F: 0},
	{F3F3F3F3F3F_3F3F3F3F3F3F_3F3F3F3F3F3F3F3F3F3F_3F3F3F3F3F3F3F: 0},
	{F3F3F3F3F3F3F3F3F3F3F_3F3F3F3F3F3F3F3F3F3F: 0},
	{Хранитель: 0},
	{Спрайт10: 0},
	{КнопкаСтарт: 0},
	{МапаТайлівМеню: 0},
	{Basalt_28side_texture29_JE1_BE2: 0},
	{pngklevclubla0kpportalmainkraftpng: 0},
	{Спрайт11: 0},
	{ПлиточнийФон: 0},
	{Спрайт12: 0},
	{Стрела_предмет_JE1_BE: 0},
	{c479ac376f71439d7b984a758fd48b2d_w: 0},
	{аНІМАЦІЯВИБУХУ: 0},
	{Спрайт13: 0},
	{Спрайт14: 0},
	{Спрайт15: 0},
	{Спрайт16: 0},
	{Спрайт17: 0},
	{Скалковый_катализатор_верхняя_текстура_JE1_BE: 0},
	{Спрайт18: 0},
	{Спрайт19: 0},
	{istockphoto185005145612x: 0},
	{darkblackbackgrounddesignwithstripes_: 0},
	{download: 0},
	{download2: 0},
	{download3: 0},
	{download4: 0},
	{download5: 0},
	{download6: 0},
	{download7: 0},
	{download8: 0},
	{download9: 0},
	{F3F3F3F3F3F3F: 0},
	{"3DФорма": 0},
	{Спрайт20: 0},
	{Спрайт21: 0},
	{Спрайт22: 0},
	{Snifflet_sniff_pixel_art: 0},
	{bad21a23bbdeebf9014e82d11c: 0},
	{images: 0},
	{images2: 0},
	{images3: 0},
	{Спрайт23: 0},
	{Ракета_Texture_Update: 0}
];

self.InstanceType = {
	Стіна: class extends self.ITilemapInstance {},
	Підлога: class extends self.ITilemapInstance {},
	RoboCat: class extends self.ISpriteInstance {},
	Keyboard: class extends self.IInstance {},
	камера: class extends self.ISpriteInstance {},
	Миша: class extends self.IInstance {},
	Приціл: class extends self.ISpriteInstance {},
	Пуля: class extends self.ISpriteInstance {},
	Зброя: class extends self.ISpriteInstance {},
	Колючка: class extends self.ISpriteInstance {},
	Привид: class extends self.ISpriteInstance {},
	привидХП: class extends self.ISpriteInstance {},
	__InvalidName0__: class extends self.ISpriteInstance {},
	Спрайт: class extends self.ISpriteInstance {},
	Спрайт2: class extends self.ISpriteInstance {},
	Аудіо: class extends self.IInstance {},
	Спрайт3: class extends self.ISpriteInstance {},
	Спрайт4: class extends self.ISpriteInstance {},
	F3F3F3F3F_3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F3F: class extends self.ISpriteInstance {},
	maska_golova_minecraft_kriper_karton_: class extends self.ISpriteInstance {},
	deepdarkcaves: class extends self.ISpriteInstance {},
	tmb_356066_: class extends self.ISpriteInstance {},
	F3F3F3F3F3F3F3F3F_3F3F3F3F3F: class extends self.ISpriteInstance {},
	Sculk_Shrieker_BE: class extends self.ISpriteInstance {},
	Deepslate_Tiles_JE: class extends self.ISpriteInstance {},
	Polished_Deepslate_28texture29_JE: class extends self.ISpriteInstance {},
	Deepslate_Tiles_28texture29_JE: class extends self.ISpriteInstance {},
	СТРЕЛА: class extends self.ISpriteInstance {},
	Basalt_28side_texture29_JE1_BE: class extends self.ISpriteInstance {},
	Спрайт5: class extends self.ISpriteInstance {},
	Спрайт6: class extends self.ISpriteInstance {},
	Спрайт7: class extends self.ISpriteInstance {},
	F3F3F3F3F3F3F3F3F3F3F_3F3F3F3F3F3F: class extends self.ISpriteInstance {},
	Спрайт8: class extends self.ISpriteInstance {},
	Спрайт9: class extends self.ISpriteInstance {},
	F3F3F3F3F: class extends self.ISpriteInstance {},
	F3F3F3F3F3F_3F3F3F3F3F3F_3F3F3F3F3F3F3F3F3F3F_3F3F3F3F3F3F3F: class extends self.ISpriteInstance {},
	F3F3F3F3F3F3F3F3F3F3F_3F3F3F3F3F3F3F3F3F3F: class extends self.ISpriteInstance {},
	Хранитель: class extends self.ISpriteInstance {},
	Спрайт10: class extends self.ISpriteInstance {},
	КнопкаСтарт: class extends self.IButtonInstance {},
	МапаТайлівМеню: class extends self.ITilemapInstance {},
	Basalt_28side_texture29_JE1_BE2: class extends self.ISpriteInstance {},
	pngklevclubla0kpportalmainkraftpng: class extends self.ISpriteInstance {},
	Спрайт11: class extends self.ISpriteInstance {},
	ПлиточнийФон: class extends self.ITiledBackgroundInstance {},
	Спрайт12: class extends self.ISpriteInstance {},
	Стрела_предмет_JE1_BE: class extends self.ISpriteInstance {},
	c479ac376f71439d7b984a758fd48b2d_w: class extends self.ISpriteInstance {},
	аНІМАЦІЯВИБУХУ: class extends self.ISpriteInstance {},
	Спрайт13: class extends self.ISpriteInstance {},
	Спрайт14: class extends self.ISpriteInstance {},
	Спрайт15: class extends self.ISpriteInstance {},
	Спрайт16: class extends self.ISpriteInstance {},
	Спрайт17: class extends self.ISpriteInstance {},
	Скалковый_катализатор_верхняя_текстура_JE1_BE: class extends self.ISpriteInstance {},
	Спрайт18: class extends self.ISpriteInstance {},
	Спрайт19: class extends self.ISpriteInstance {},
	istockphoto185005145612x: class extends self.ISpriteInstance {},
	darkblackbackgrounddesignwithstripes_: class extends self.ISpriteInstance {},
	download: class extends self.ISpriteInstance {},
	download2: class extends self.ISpriteInstance {},
	download3: class extends self.ISpriteInstance {},
	download4: class extends self.ISpriteInstance {},
	download5: class extends self.ISpriteInstance {},
	download6: class extends self.ISpriteInstance {},
	download7: class extends self.ISpriteInstance {},
	download8: class extends self.ISpriteInstance {},
	download9: class extends self.ISpriteInstance {},
	F3F3F3F3F3F3F: class extends self.ISpriteInstance {},
	_3DФорма: class extends self.I3DShapeInstance {},
	Спрайт20: class extends self.ISpriteInstance {},
	Спрайт21: class extends self.ISpriteInstance {},
	Спрайт22: class extends self.ISpriteInstance {},
	Snifflet_sniff_pixel_art: class extends self.ISpriteInstance {},
	bad21a23bbdeebf9014e82d11c: class extends self.ISpriteInstance {},
	images: class extends self.ISpriteInstance {},
	images2: class extends self.ISpriteInstance {},
	images3: class extends self.ISpriteInstance {},
	Спрайт23: class extends self.ISpriteInstance {},
	Ракета_Texture_Update: class extends self.ISpriteInstance {}
}