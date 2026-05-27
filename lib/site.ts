export const site = {
  name: "Discord.py Components V2 Guide",
  subtitle: "A premium discord.py 2.x academy, reference, and production handbook for modern interactions.",
  description:
    "Modern discord.py 2.x Components learning ecosystem with academy lessons, production architecture, references, and verified Python examples.",
  repoName: "discordpy-components-v2-guide",
  owner: "itzadhi",
  primary: "discord.py 2.x",
  language: "Python",
  credit: {
    username: "itzaqdhi",
    displayName: "Adhi",
    githubUrl: "https://github.com/itzadhi"
  },
  url: "https://itzadhi.github.io/discordpy-components-v2-guide/",
  repoUrl: "https://github.com/itzadhi/discordpy-components-v2-guide",
  docsUrl: "https://itzadhi.github.io/discordpy-components-v2-guide/docs",
  logo: "/brand/adhi-logo.jpeg",
  ogImage: "/og/social-card.svg",
  references: [
    { label: "Discord Components Overview", href: "https://docs.discord.com/developers/components/overview" },
    { label: "Discord Component Reference", href: "https://docs.discord.com/developers/components/reference" },
    { label: "discord.py Interactions API", href: "https://discordpy.readthedocs.io/en/stable/interactions/api.html" }
  ]
} as const;

export function assetPath(path: string) {
  const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
  const normalized = path.startsWith("/") ? path : `/${path}`;
  return `${base}${normalized}`;
}
