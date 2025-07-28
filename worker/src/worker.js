// Cloudflare Worker Code - Now a Scheduler
export default {
  async fetch(request, env, ctx) {
    // This part handles manual runs or tests
    console.log("Worker triggered by an HTTP request.");
    await triggerGitHubAction(env);
    return new Response('OK. GitHub Action triggered.');
  },

  async scheduled(controller, env, ctx) {
    // This part handles the cron trigger
    console.log("Worker triggered by a cron schedule.");
    await triggerGitHubAction(env);
  },
};

async function triggerGitHubAction(env) {
  const GITHUB_REPO = 'glitchood/notion-gtasks-sync';
  const GITHUB_PAT = env.GITHUB_PAT;

  await fetch(`https://api.github.com/repos/${GITHUB_REPO}/dispatches`, {
    method: 'POST',
    headers: {
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': `token ${GITHUB_PAT}`,
      'User-Agent': 'Cloudflare-Worker-Scheduler',
    },
    body: JSON.stringify({
      // We trigger our NEW action
      event_type: 'poll-trigger', 
      client_payload: {
        "triggered_by": "Cloudflare Cron"
      }
    }),
  });
}